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
    
def getUserByName(username):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        print("Username:", username)
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        print("User", user)
        if user == None:
            return None
        user1 = {
            'id': user[0],
            'username': user[1],
            'age': user[3],
            'email': user[4],
            'address': user[5],
            'allowVisit': user[6]
        }
        print(user1)
        conn.commit()
        conn.close()
        return user1
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

def getUser(id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", str(id))
        user = cursor.fetchone()
        # print(user)
        conn.close()
        user_info = []
        
        if user != None:
            user_info = {
                'id': user[0],
                'username': user[1],
                'age': user[3],
                'email': user[4],
                'address': user[5],
                'allowVisit': user[6]
            }
            # user_info['id'] = user[0]
            # user_info['username'] = user[1]
            # user_info['age'] = user[3]
            # user_info['email'] = user[4]
            # user_info['address'] = user[5]
            # user_info['allowVisit'] = user[6]
            print(user_info)
            return user_info
        else:
            return "Không tìm thấy user!"
    except Exception as e:
        return str(e)
