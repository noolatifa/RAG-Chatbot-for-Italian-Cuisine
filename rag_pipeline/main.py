from loader import load_data
from vectorstore import VectorStore
from retriever import Retriever
from llmgenerator import LLMGenerator
from config import VECTOR_DB_PATH
from chat_history import init_db, save_chat, get_last_chats  # gestion historique

# Initialize chat history DB
init_db()

# Load and prepare data
documents = load_data()

# Initialize vector store and add documents
vector_store = VectorStore(VECTOR_DB_PATH)
vector_store.add_documents(documents)

# Initialize components
retriever = Retriever(vector_store)
llm_generator = LLMGenerator()

# Chat loop with Italian cuisine-specific logic
print("Chatbot is ready! Type 'exit' to quit.")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        context = retriever.get_relevant_docs(user_input)
        if not context:
            print("Bot: I'm only trained to answer questions related to Italian cuisine. Please ask me something about Italian cuisine!")
            continue

        context_text = context[0].page_content

        # Ajout de l'historique
        history = get_last_chats(3)
        history_text = "\n".join([f"User: {u}\nBot: {b}" for u, b in history])

        prompt = f"""
        You are a friendly AI assistant specializing in Italian cuisine. While you can answer **basic conversational questions** (e.g., "Who are you?"), your primary focus is **Italian cuisine**. 

        ### **Instructions:**  
        - **Use the provided context** when available. If no relevant context exists, say: *"I don't know."*  
        - **For greetings & personal questions ("Who are you?")**, answer briefly and naturally. Example:  
        - User: "Who are you?"  
        - Bot: "I'm an AI assistant designed to chat about Italian cuisine! Ask me anything about recipes, history, or fun food facts."  
        - **If a question is slightly off-topic** but still general (e.g., "What's the capital of Italy?"), give a **brief answer** and immediately bring the topic back to Italian cuisine. Example:  
        - User: "Do you like movies?"  
        - Bot: "Movies are great! Speaking of great things, did you know Italian cuisine inspired many famous dishes in films?"  
        - **If the question is completely unrelated to Italian cuisine (e.g., coding, technology, or cars), do not engage.** Example:  
        - User: "Can you explain Python code?"  
        - Bot: "I specialize in Italian cuisine topics! But if you're interested, I can share a great Italian recipe instead."  
        - **If the user keeps asking off-topic questions, remind them:**  
        - "I love chatting, but my knowledge is focused on Italian cuisine! Let’s talk about that."  
        
        ### **Special note about short answers:**
        - If the user's input is a short answer like "yes", "no", "maybe", or similar, **assume it refers to your last question or proposal.**
        - Before answering, **briefly restate or paraphrase your last question** to confirm the context.
        - Then provide the appropriate follow-up based on the user's short answer.

        ### **Chat History:**  
        {history_text}

        ### **Context:**  
        Text: {context_text}  

        ### **User Input:**  
        User: {user_input}  
        Bot:
        """

        response = llm_generator.generate_response(prompt)
        print("Bot:", response)

        #Sauvegarde en base
        save_chat(user_input, response)

    except Exception as e:
        print(f"An error occurred: {e}")
