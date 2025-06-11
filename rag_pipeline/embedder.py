from langchain_ollama import OllamaEmbeddings
from config import OLLAMA_MODEL

def get_embeddings():
    """Returns an embeddings instance for Ollama."""
    return OllamaEmbeddings(model=OLLAMA_MODEL)