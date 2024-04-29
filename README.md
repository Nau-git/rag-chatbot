# Raggy: The Prompt Engineering Guru 🧙‍♂️🪄

Welcome to my second llm-powered project where I build a simple RAG (Retrieval-Augmented Generation) chatbot. I call the chatbot "Raggy". It is designed to answer questions about prompt engineering.

## Motivation ✍️

With the emergence of large language models (LLMs) like ChatGPT, one of the main challenges has been the propensity for hallucination – generating responses that contradict or lack grounding in factual information. Retrieval Augmented Generation (RAG) has been one of the most promising approaches to mitigate this issue, aiming to ground the chatbot's responses by incorporating relevant information from external sources. Developing a RAG chatbot presents an opportunity to explore techniques for enhancing the factual accuracy and grounding of LLM-based systems. Moreover, this project aligns with my keen interest in developing applications based on cutting-edge language models.

## Under the Hood 🔧

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
3. Set up your environment variables (e.g., API keys)
4. Start the app: `chainlit run app/chatbot.py`
5. Open the app in your browser and start chatting with Raggy!

## Hugging Face Spaces 🤗

Raggy is deployed on [Hugging Face Spaces](https://huggingface.co/spaces/naaufal/raggy)

![preview](https://github.com/Nau-git/rag-chatbot/blob/main/image/raggy.png)

## Resources 📚

- [promptingguide.ai](https://promptingguide.ai) 
- [Amogh Agastya's article on using Langchain for RAG](https://betterprogramming.pub/harnessing-retrieval-augmented-generation-with-langchain-2eae65926e82)
- [List of embedding model](https://www.sbert.net/docs/pretrained_models.html)
- [Fullstackretrieval by Greg Kamradt](https://fullstackretrieval.com)

