from langchain_chroma import Chroma
from embedder import get_embeddings
from config import VECTOR_DB_PATH
from langchain.schema import Document

class VectorStore:
    def __init__(self, db_path):
        self.store = Chroma(persist_directory=db_path, embedding_function=get_embeddings())
    
    def add_documents(self, texts):
        """Adds text values to the vector store."""
        documents = [Document(page_content=text) for text in texts]
        self.store.add_documents(documents)
    
    def as_retriever(self):
        """Returns the retriever for the vector store."""
        return self.store.as_retriever()