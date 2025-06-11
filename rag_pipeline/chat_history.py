import sqlite3

DB_PATH = "history/chat_history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_chat(user_input, bot_response):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO history (user_input, bot_response) VALUES (?, ?)", (user_input, bot_response))
    conn.commit()
    conn.close()

def get_last_chats(n=5):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT user_input, bot_response FROM history ORDER BY timestamp DESC LIMIT ?", (n,))
    rows = c.fetchall()
    conn.close()
    #chronological order
    return list(reversed(rows))
