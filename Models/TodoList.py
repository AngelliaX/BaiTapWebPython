import sqlite3
from flask import g
import os
import html

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
        cursor.execute("SELECT * FROM todolists WHERE userId = ?",  userId)
        # cursor.execute(query)
        # conn.commit()
        todos = cursor.fetchall()
        todolist = []
        print("Length: ", len(todos))
        print("Todos: ", todos)
        for row in todos:
            print(row[0])
            todo = {"id": row[0], "title": row[1], "data": row[2], "status": row[3], "userId": row[4]}
            todolist.append(todo)
        # print(todos)
        conn.close()
        return todolist
    except Exception as e:
        return str(e)

def get_todo_by_id(id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        query = "SELECT * FROM todolists WHERE id = " + id
        # print(query)
        cursor.execute(query)
        conn.commit()
        todo = cursor.fetchone()
        todolist = []
        todo = {"id": todo[0], "title": todo[1], "data": todo[2], "status": todo[3], "userId": todo[4]}
        todolist.append(todo)
        conn.close()
        return todolist
    except Exception as e:
        return str(e)
    
def updateTodo(title, data, status, id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        # query = "UPDATE todolists SET title = " + title + ", data = " + data + ", status = " + status + " WHERE id = " + id
        # print(query)
        cursor.execute('''
                       UPDATE todolists 
                       SET title = ?, data = ?, status = ?
                       WHERE id = ?
                    ''', (title, data, status, id))
        # cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return str(e)
    
def removeTodo(id):
    try:
        print(id)
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        query = "DELETE FROM todolists WHERE id = " + id
        print(query)
        cursor.execute('''
                       DELETE FROM todolists 
                       WHERE id = ?
                    ''', id)
        # cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return str(e)
    
def insertTodo(id, title, data, status, userId):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        # print(query)
        cursor.execute('''
                       INSERT INTO todolists VALUES(?, ?, ?, ?, ?)
                    ''', (id, title, data, status, userId))
        # cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return str(e)