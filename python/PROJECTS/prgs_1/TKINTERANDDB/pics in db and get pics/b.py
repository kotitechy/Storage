import tkinter as tk
from tkinter import filedialog
import sqlite3

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        insert_image_into_database(file_path)

def insert_image_into_database(file_path):
    with open(file_path, 'rb') as image_file:
        image_data = image_file.read()
        
        conn = sqlite3.connect('image_db.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO images (image_data) VALUES (?)', (image_data,))
        conn.commit()
        conn.close()

# Create the main window
root = tk.Tk()
root.title("Image to Database")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open Image", command=open_file_dialog)
open_button.pack()

# Start the main event loop
root.mainloop()
