# Raggy: The Prompt Engineering Guru 🧙‍♂️🪄

Welcome to my second llm-powered project. Introducing Raggy, your friendly neighborhood RAG (Retrieval-Augmented Generation) chatbot! 🤖 Raggy is here to help you unlock the power of language models through killer prompts. 🔥

## About Raggy 🐶

Raggy is a chatbot app powered by large language model and leveraging retrieval-augmented generation technique. Its knowledge base is sourced from [promptingguide.ai](https://promptingguide.ai), a comprehensive resource on prompt engineering.

Whether you're a total newbie or a seasoned pro, Raggy's got your back! 🙌 From understanding prompt structure and elements to exploring advanced techniques like few-shot learning and chain-of-thought prompting, Raggy can guide you through it all with fun and easy-to-understand explanations. 💡

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


## Acknowledgments 🙏

- [promptingguide.ai](https://promptingguide.ai) for providing the knowledge base for Raggy.
- [Open-Source Libraries Used](CREDITS.md) for the open-source libraries and frameworks used in this project.

Let's create some prompting magic together! 🧙‍♂️🪄