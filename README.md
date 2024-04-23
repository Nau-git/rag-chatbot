RAG has been one of the popular ways to build with LLMs

The parts: data, embedding model, vector store, ...

Resources:
- https://discover.fullstackretrieval.com
- https://rungalileo.io/blog/mastering-rag-how-to-architect-an-enterprise-rag-system                <<< includes 7 challenges in RAG
- https://rungalileo.io/blog/mastering-rag-llm-prompting-techniques-for-reducing-hallucinations     <<< ref about LLM prompting techniques for RAG
- https://www.sbert.net/docs/pretrained_models.html                                                 <<< ref in selecting embedding model
- https://huggingface.co/spaces/mteb/leaderboard                                                    <<< another ref for selecting embedding model
- https://rungalileo.io/blog/fix-hallucinations-in-rag-systems-with-pinecone-and-galileo            <<< explanation about embedding in the youtube video


Machine learning materials:
- https://machinelearningmastery.com/start-here/ 






# Raggy: The Prompt Engineering Guru 🧙‍♂️🪄

Welcome to the official GitHub repository of Raggy, your friendly neighborhood RAG (Retrieval-Augmented Generation) chatbot! 🤖 Raggy is here to help you unlock the power of language models through killer prompts. 🔥

## About Raggy 🐶

Raggy is a chatbot app powered by state-of-the-art language models and retrieval-augmented generation techniques. Its knowledge base is sourced from [promptingguide.ai](https://promptingguide.ai), a comprehensive resource on prompt engineering.

Whether you're a total newbie or a seasoned pro, Raggy's got your back! 🙌 From understanding prompt structure and elements to exploring advanced techniques like few-shot learning and chain-of-thought prompting, Raggy can guide you through it all with fun and easy-to-understand explanations. 💡

## Under the Hood 🔧

Raggy is built using the following technologies:

- **Language Model**: gpt-3.5-turbo is used as the large language model (LLM) to generate responses.
- **Vector Database**: Chromadb is employed as the vector database to store and retrieve relevant knowledge from the knowledge base.
- **Embedding Model**: The all-MiniLM-L6-v2 model is used for generating embeddings from the text data.
- **HTML Loader**: The RecursiveUrlLoader is used for loading and processing the HTML content from promptingguide.ai.
- **Text Splitter**: The RecursiveCharacterTextSplitter is utilized for splitting the text data into smaller chunks for efficient processing.

## Getting Started 🚀

To get started with Raggy, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/raggy.git`
2. Install the required dependencies: `npm install`
3. Set up your environment variables (e.g., API keys)
4. Start the app: `npm start`
5. Open the app in your browser and start chatting with Raggy!

## Contributing 🤝

We welcome contributions from the community! If you'd like to contribute to Raggy, please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b my-new-feature`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## License 📄

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments 🙏

- [promptingguide.ai](https://promptingguide.ai) for providing the knowledge base for Raggy.
- [Open-Source Libraries Used](CREDITS.md) for the open-source libraries and frameworks used in this project.

Let's create some prompting magic together! 🧙‍♂️🪄