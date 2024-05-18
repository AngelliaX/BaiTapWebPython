import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('SQLITE3.db')
cursor = conn.cursor()

# Create users table with unique constraint on username
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
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