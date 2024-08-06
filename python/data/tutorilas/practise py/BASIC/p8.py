import tkinter as tk
from tkinter import messagebox

def greet():
    name = name_entry.get()
    messagebox.showinfo("Greeting", f"Hello, {name}!")

# Create the main window
root = tk.Tk()
root.title("Greeting App")
root.geometry('300x300')
# Create and add widgets to the main window
label = tk.Label(root, text="Enter your name:")
label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack()

# Run the main event loop
root.mainloop()
