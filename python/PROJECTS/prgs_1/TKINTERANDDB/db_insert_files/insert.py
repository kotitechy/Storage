import sqlite3
 
def to_binary(filename):
    '''Convert data to binary format'''
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data
 
def insert_blob(emp_id, name, audio, resume_file):
    try:
        sqlite_connection = sqlite3.connect('audio.db')
        cursor = sqlite_connection.cursor()
        print("Connected to SQLite")
        sqlite_query = "INSERT INTO audio_table (id, name, audio, resume) VALUES (?, ?, ?, ?)"
        emp_audio = to_binary(audio)
        resume = to_binary(resume_file)
        # Convert data into tuple format
        data_tuple = (emp_id, name, emp_audio, resume)
        cursor.execute(sqlite_query, data_tuple)
        sqlite_connection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
 
    except sqlite3.Error as error:
        print(f"Failed to insert blob data into sqlite table {error}")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The sqlite connection is closed")



insert_blob(1, "hello","gs1.mp3", "p1.txt")


insert_blob(2, "Clean Bandit", "gs1.mp3", "p1.txt")