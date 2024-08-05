from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

db_path = os.path.join(os.path.dirname(__file__), 'todo.db')

def initialize_database():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, task TEXT, created_at TEXT)''')
    conn.commit()
    conn.close()

@app.before_request
def before_request():
    initialize_database()

@app.template_filter('datetimeformat')
def datetimeformat(value):
    dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%H:%M %d.%m.%y")

@app.route('/')
def index():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks, message='')

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task'].strip()
    if not task:
        return render_template('index.html', tasks=get_tasks(), message='Поле ввода текста не может быть пустым')

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task, created_at) VALUES (?, ?)', (task, created_at))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

def get_tasks():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks

if __name__ == '__main__':
    app.run(debug=True)
