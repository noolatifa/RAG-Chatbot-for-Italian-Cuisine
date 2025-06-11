from langchain_ollama import OllamaLLM
from config import OLLAMA_MODEL

class LLMGenerator:
    def __init__(self):
        self.llm = OllamaLLM(model=OLLAMA_MODEL)#pulling the llama model as init
    
    def generate_response(self, prompt):
        """Generates a response using the LLM."""
        try:
            return self.llm.invoke(prompt) #kima "await axios.post('/api', { prompt" in js
        except Exception:
            return "There was an issue processing your request."