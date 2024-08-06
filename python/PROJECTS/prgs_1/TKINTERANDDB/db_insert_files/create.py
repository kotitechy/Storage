import sqlite3
 
conn = sqlite3.connect('audio.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS AUDIO")
 
# Creating table as per requirement
sql = "CREATE TABLE audio_table (id, name TEXT NOT NULL, audio BLOB NOT NULL, resume BLOB NOT NULL);"
cursor.execute(sql)
print("Table created successfully.....")