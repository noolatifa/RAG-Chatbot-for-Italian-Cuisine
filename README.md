# RAG Chatbot for Italian Cuisine 🇮🇹

This project implements a Retrieval-Augmented Generation (RAG) chatbot focused on Italian cuisine.  
It uses a vector database and a language model to answer user queries about recipes, ingredients, cooking techniques, and regional specialties.  

The chatbot’s knowledge base is powered by a JSON file, which can be extended with more data to improve the quality and scope of responses.

---

## How to Run the Project

Before running the chatbot, make sure to set up the required folders:

### Required Folders

Create the following folders inside the `rag_pipeline/` directory:

```bash
mkdir -p rag_pipeline/history
mkdir -p rag_pipeline/vector_db

To run the chatbot in the console, use:
python main.py

To run the chatbot with a Graphical User Interface (GUI) using Streamlit, use:
streamlit run app.py
