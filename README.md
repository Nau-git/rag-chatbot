# Raggy: The RAG Chatbot 🤖🪄

Welcome to my second llm-powered project where I build a simple RAG (Retrieval-Augmented Generation) chatbot. I call the chatbot "Raggy". It is designed to answer questions about prompt engineering.

## Motivation ✍️

With this project, I'd like to demonstrate my skill in using emerging AI tools such as ChromaDB, Hugging Face, Chainlit, and Langchain.


## Under the Hood 🔧

![Components](https://github.com/Nau-git/rag-chatbot/blob/main/images/RAG_comp.png)

The chatbot is comprised of several components as shown in above diagram.

The first is the **Knowledge Base**. It is the source of information that will be used to answer questions. It can be in many format such as doc, txt, html, pdf, and so on. There is a lot of growing interest of using pdf as the knowledge base. However, I found that the pdf is not well-suited for the this task due to the structure of the pdf. It is hard to extract the relevant information especially if the pdf contains a lot of images. Therefore, in this project I choose to have html (the [Promptingguide](https://www.promptingguide.ai/)) as the knowledge base.

The URL (and the child links) are then loaded using Langchain's RecursiveUrlLoader. The loaded contents (text) are still raw, so they are processed to remove unnecessary tags and spaces. 

The next step is splitting/chunking. There are several ways to split the text into **chunks**. In this project, I use the Langchain's RecursiveCharacterTextSplitter. The splitting is done based on the character length. The splitter will recursively split the text into smaller chunks until the chunk size is less than the specified character length. The chunk size is set to 2500 characters in this project.

The next step is generating embeddings from the text data. The embeddings are generated using an **embedding model**. There are a lot of options out there, OpenAI's text-embedding-large is probrably the best one yet (at the time of writing this), but it is in the cloud (access through API) and is not free. For the open sourced ones, we can refer to Hugging Face's Massive Text Embedding Benchmark (MTEB) as well as the SentenceTransformers website. Considering the average speed and the size, I choose the all-MiniLM-L6-v2 model.

The chunks are all converted into vector representations using the embedding model and then stored in a vector store. Once again, there are a lot of options for this. I choose Chromadb because it is open sourced.




> natural language understanding
> multi-turn chat
> give source document



Raggy is built using the following technologies:

- **Language Model**: gpt-3.5-turbo is used as the large language model (LLM) to generate responses.
- **Vector Database**: Chromadb is employed as the vector database to store and retrieve relevant knowledge from the knowledge base.
- **Embedding Model**: The all-MiniLM-L6-v2 model is used for generating embeddings from the text data.
- **HTML Loader**: The RecursiveUrlLoader is used for loading and processing the HTML content from promptingguide.ai.
- **Text Splitter**: The RecursiveCharacterTextSplitter is utilized for splitting the text data into smaller chunks.

## Getting Started 🚀

To get started with Raggy, follow these steps:

1. Clone the repository: `git clone https://github.com/Nau-git/rag-chatbot.git`
2. Install the required dependencies: `poetry install`
3. Set up your environment variables (e.g., API keys) in a .env file (see.env.example)
4. Start the app: `chainlit run app/chatbot.py`
5. Open the app in your browser and start chatting with Raggy!

## Hugging Face Spaces 🤗

Raggy is deployed on [Hugging Face Spaces](https://huggingface.co/spaces/naaufal/raggy)

![preview](https://github.com/Nau-git/rag-chatbot/blob/main/images/raggy.png)

## Resources 📚

- [promptingguide.ai](https://promptingguide.ai) 
- [Amogh Agastya's article on using Langchain for RAG](https://betterprogramming.pub/harnessing-retrieval-augmented-generation-with-langchain-2eae65926e82)
- [List of pre-trained embedding model in SentenceTransformers](https://www.sbert.net/docs/pretrained_models.html)
- [Massive Text Embedding Benchmark](https://huggingface.co/spaces/mteb/leaderboard)
- [Fullstackretrieval by Greg Kamradt](https://community.fullstackretrieval.com)

