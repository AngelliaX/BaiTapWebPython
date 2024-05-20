import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('SQLITE3.db')
cursor = conn.cursor()

# Create users table with unique constraint on username
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL
#     )
# ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
		age INTEGER,
		email TEXT,
		address TEXT,
		allowVisit BOOLEAN NOT NULL CHECK (allowVisit IN (0, 1)) DEFAULT 1
    )             
''')
cursor.execute('''
    PRAGMA foreign_keys = ON;
    
    CREATE TABLE IF NOT EXISTS todolists (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOTE NULL,
		data TEXT,
		status INTEGER,
		userId INTEGER NOT NULL,
		FOREIGN KEY (userId) REFERENCES users(id)
    )            
''')
# Insert a sample user into the users table
try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("sample_user", "sample_password"))
    print("Sample user inserted successfully!")
except sqlite3.IntegrityError as e:
    print(f"Error inserting sample user: {e}")

# Commit changes and close connection
conn.commit()
conn.close()