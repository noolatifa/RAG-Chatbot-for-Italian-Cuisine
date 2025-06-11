#logique de récuperation de documents
# convertit le vector store en un "retriever" standard LangChain using return as retriever
# puis utilise .invoke() pour récupérer les documents pertinents pour le user input 

from langchain_chroma import Chroma

class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store
    
    def get_relevant_docs(self, query):
        """Retrieves relevant documents based on the query."""
        return self.vector_store.as_retriever().invoke(query)