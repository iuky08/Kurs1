import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'todo.db')

def create_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, task TEXT, created_at TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
