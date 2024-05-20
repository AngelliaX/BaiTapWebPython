import sqlite3
from flask import g
import os

data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database')
DATABASE = os.path.join(data_folder, 'SQLITE3.db')

# Create database
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS todolists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        title TEXT NOTE NULL,
        data TEXT,
        status INTEGER,
        userId INTEGER,
        FOREIGN KEY(userId) REFERENCES users(id) 
    )
''')

conn.commit()
conn.close()

def add_todo(title, description, status, userId):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO todolists VALUES (?, ?, ?, ?)", title, description, status, userId)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return str(e)

def get_todo_list(userId):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        query = "SELECT * FROM todolists WHERE userId = " + userId
        print(query)
        # cursor.execute("SELECT * FROM todolists WHERE userId = ?",  userId)
        cursor.execute(query)
        # conn.commit()
        todos = cursor.fetchall()
        print("Length: ", len(todos))
        print("Todos: ", todos)
        for row in todos:
            print(row)
            
        # print(todos)
        conn.close()
        return todos
    except Exception as e:
        return str(e)
