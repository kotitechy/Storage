import sqlite3
 
def write_file(data, filename):
    '''Convert binary data and write it on Hard Disk'''
    with open(filename, 'wb') as file:
        file.write(data)
    print(f"Stored blob data into:{filename}\n")
 
def read_blob(emp_id, audio_path, describe_path):
    try:
        sqlite_con = sqlite3.connect('audio.db')
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")
        sql_blob_query = "SELECT * from audio_table where id = ?"
        cursor.execute(sql_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            name  = row[1]
            photo = row[2]
            resumeFile = row[3]
            print("Storing employee image and resume on disk \n")
 
            audio = f"{audio_path}{name}.mp3"
            describe = f"{describe_path}{name}.txt"
            write_file(photo, audio)
            write_file(resumeFile, describe)
        cursor.close()
 
    except sqlite3.Error as error:
        print(f"Failed to read blob data from sqlite table {error}")
    finally:
        if sqlite_con:
            sqlite_con.close()
            print("sqlite connection is closed")
 
if __name__ == '__main__':
    audio_path = "C:\Users\shiva\Documents\db\audio\"
    describe_path = "C:\Users\shiva\Documents\db\audio\"
    read_blob(1, audio_path, describe_path)
    read_blob(2, audio_path, describe_path)