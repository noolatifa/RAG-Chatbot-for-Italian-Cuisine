
import streamlit as st
from core import build_components, generate_bot_response
from chat_history import get_last_chats

# entete perso
st.set_page_config(page_title="AlDente", page_icon="🍝")

# CSS DESIGNN
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
       

        }
        .main-container {
            display: flex;
            justify-content: center;
            margin-top: 30px;
                 border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        }
   
        .message {
            padding: 15px 20px;
            border-radius: 20px;
            margin: 10px 0;
            max-width: 75%;
            line-height: 1.5;
        }
        .user {
            background-color: #FFF9DB;
            align-self: flex-end;
            text-align: left;
            margin-left: auto;
            color: #000000;
            width: fit-content;         
            max-width: 80%;            
            word-wrap: break-word; 
        }
        .bot {
            background-color: #FFECEC;
            align-self: flex-start;
            text-align: left;
            margin-right: auto;
            color: #000000;
        }
        .chat-wrapper {
            display: flex;
            flex-direction: column;
        }
            h1 {
            text-align: center;
            color: #222;
            font-size: 2.5rem;
        }
        h1 span {
            color: #F28C8C;
        }
    </style>
""", unsafe_allow_html=True)

# H1 TITLE
st.markdown('<h1 style="text-align:center;">🍝 Meet <span>AlDente</span>, your Italian Cuisine assistant</h1>', unsafe_allow_html=True)

# Initialisation des composants
if "retriever" not in st.session_state:
    retriever, llm_generator = build_components()
    st.session_state.retriever = retriever
    st.session_state.llm_generator = llm_generator

with st.container():
    st.markdown('<div class="main-container"><div class="chat-wrapper">', unsafe_allow_html=True)

    # Historique (plus ancien > plus récent)
    for u, b in get_last_chats(5):
        st.markdown(f'<div class="message user"><strong>You :</strong><br>{u}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="message bot"><strong>AlDente :</strong><br>{b}</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Posez-moi une question sur la cuisine italienne...")

if user_input:
    # Affiche le message utilisateur
    st.markdown(f'<div class="main-container"><div class="chat-wrapper">', unsafe_allow_html=True)
    st.markdown(f'<div class="message user"><strong>You :</strong><br>{user_input}</div>', unsafe_allow_html=True)

    # Génère et affiche la réponse du bot
    response = generate_bot_response(user_input, st.session_state.retriever, st.session_state.llm_generator)
    st.markdown(f'<div class="message bot"><strong>AlDente :</strong><br>{response}</div>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
