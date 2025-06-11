#  RAG Chatbot for Italian Cuisine 🇮🇹

This project implements a **Retrieval-Augmented Generation (RAG) chatbot** specialized in Italian cuisine. It uses a vector database and a language model to answer user queries about recipes, ingredients, cooking techniques, and regional specialties.
The JSON file powers the knowledge base.
It can be extended with more data to improve the chatbot’s answers.
---

##  How to Run the Project

Before running the chatbot, make sure to set up the required folders:

###  Required Folders

Create the following folders inside the `rag_pipeline/` directory:

```bash
mkdir -p rag_pipeline/history
mkdir -p rag_pipeline/vector_db
