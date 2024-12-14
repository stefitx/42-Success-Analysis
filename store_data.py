import sqlite3

# Connect to or create the SQLite database
conn = sqlite3.connect('42_school_data.db')
cursor = conn.cursor()

# Create a table (modify columns as per your data structure)
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  login TEXT,
                  displayname TEXT,
                  cursus TEXT
                  )''')

# Insert data into the table
cursor.execute('INSERT INTO users (id, login, displayname, cursus) VALUES (?, ?, ?, ?)',
               (user_data['id'], user_data['login'], user_data['displayname'], '42 Cursus'))

# Commit and close connection
conn.commit()
conn.close()
