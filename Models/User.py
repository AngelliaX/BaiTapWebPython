import sqlite3
from flask import g
import os


data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database')
DATABASE = os.path.join(data_folder, 'SQLITE3.db')

# Create database
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

#######

def getUserByNameAndPass(username, password):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.commit()
        conn.close()
        return user
    except Exception as e:
        return str(e)


def addUser(username, password):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return str(e)



def checkUser(username, password):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return True
        else:
            return "Username hoặc password không hợp lệ!"
    except Exception as e:
        return str(e)


