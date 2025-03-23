import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Створюємо таблицю користувачів
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    selected_class TEXT
)
""")
conn.commit()

def save_user(user_id, username, selected_class):
    cursor.execute("INSERT OR REPLACE INTO users (user_id, username, selected_class) VALUES (?, ?, ?)",
                   (user_id, username, selected_class))
    conn.commit()

def get_user(user_id):
    cursor.execute("SELECT selected_class FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()