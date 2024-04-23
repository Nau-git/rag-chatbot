import re
import dotenv
import chainlit as cl
from bs4 import BeautifulSoup

from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.indexes import SQLRecordManager, index
from langchain_community.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.schema.runnable import Runnable, RunnablePassthrough, RunnableConfig
from langchain.callbacks.base import BaseCallbackHandler
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

dotenv.load_dotenv()

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", streaming=True, temperature=0.5)


def ingest_html():
    
    url = "https://www.promptingguide.ai"
    excludes = [
                "https://www.promptingguide.ai/models",
                "https://www.promptingguide.ai/risks",
                "https://www.promptingguide.ai/papers",
                "https://www.promptingguide.ai/tools",
                "https://www.promptingguide.ai/notebooks",
                "https://www.promptingguide.ai/datasets",
                "https://www.promptingguide.ai/readings",
                "https://www.promptingguide.ai/services",
                # Add other exclude URLs here
    ]
    loader = RecursiveUrlLoader(url=url, exclude_dirs=excludes)
    
    print("Loading webpages...")
    data = loader.load()
    print("Done loading!")

    def clean_html(html_content):
        # Remove unwanted HTML tags using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        cleaned_text = soup.get_text(separator=' ')
        # Remove extra whitespaces and newlines
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        return cleaned_text

    cleaned_page_content = [clean_html(x.page_content) for x in data]

    for i,j in zip(data, cleaned_page_content):
        i.page_content = j

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2500, chunk_overlap=200)
    chunks = text_splitter.split_documents(data)

    print("Creating vector store...")
    doc_search = Chroma.from_documents(chunks, embedding_model)
    print("Done creating vector store!")


    namespace = "chromadb/my_documents"
    record_manager = SQLRecordManager(
        namespace, db_url="sqlite:///record_manager_cache.sql"
    )
    record_manager.create_schema()

    index_result = index(
        chunks,
        record_manager,
        doc_search,
        cleanup="incremental",
        source_id_key="source",
    )

    print(f"Indexing stats: {index_result}")

    return doc_search

doc_search = ingest_html()

@cl.on_chat_start
async def on_chat_start():
    template = """<role>Your name is Raggy, a retrieval augmented generation (RAG) chatbot developed by Naufal (https://github.com/Nau-git). \
    You are designed to be helpful in answering queries related to prompt engineering.</role>
    
    Use the following context as the basis of your answer:

    {context}

    Say you don't know if the context don't provide enough information to answer the question. Do engage in small talks but DO NOT answer off-topic questions.
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])

    retriever = doc_search.as_retriever()

    runnable = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | chat_model
        | StrOutputParser()
    )

    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable
    msg = cl.Message(content="")

    class PostMessageHandler(BaseCallbackHandler):
        """
        Callback handler for handling the retriever and LLM processes.
        Used to post the sources of the retrieved documents as a Chainlit element.
        """

        def __init__(self, msg: cl.Message):
            BaseCallbackHandler.__init__(self)
            self.msg = msg
            self.sources = set()  # To store unique pairs

        def on_retriever_end(self, documents, *, run_id, parent_run_id, **kwargs):
            for d in documents:
                source_page_pair = (d.metadata['source'], d.metadata['title'])
                self.sources.add(source_page_pair)  # Add unique pairs to the set

        def on_llm_end(self, response, *, run_id, parent_run_id, **kwargs):
            if len(self.sources):
                sources_text = "\n".join([f"{page}#page={source}" for source, page in self.sources])
                self.msg.elements.append(
                    cl.Text(name="Sources", content=sources_text, display="inline")
                )

    async with cl.Step(type="run", name="QA Assistant"):
        async for chunk in runnable.astream(
            message.content,
            config=RunnableConfig(callbacks=[
                cl.LangchainCallbackHandler(),
                PostMessageHandler(msg)
            ]),
        ):
            await msg.stream_token(chunk)

    await msg.send()