import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk
import io  # Import the io module

# ... Rest of your code ...

def retrieve_image_from_database():
    conn = sqlite3.connect('image_db.db')
    cursor = conn.cursor()

    # Assuming 'id' is the primary key of your image table
    cursor.execute('SELECT image_data FROM images WHERE id = 1')  # Change '1' to the desired image ID
    row = cursor.fetchone()

    if row:
        image_data = row[0]
        display_image(image_data)
    else:
        print("Image not found")

    conn.close()

def display_image(image_data):
    image = Image.open(io.BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)

    image_label.configure(image=photo)
    image_label.image = photo

root = tk.Tk()
root.title("Image Viewer")

retrieve_button = ttk.Button(root, text="Retrieve Image", command=retrieve_image_from_database)
retrieve_button.pack()

image_label = ttk.Label(root)
image_label.pack()

root.mainloop()
