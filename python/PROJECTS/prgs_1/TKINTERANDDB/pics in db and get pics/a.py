import sqlite3

# Connect to the database or create a new one if it doesn't exist
conn = sqlite3.connect('image_db.db')
cursor = conn.cursor()

# Create a table to store image data
cursor.execute('CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY,image_data BLOB)')

conn.commit()
conn.close()
