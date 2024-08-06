import tkinter as tk
from tkinter import messagebox

# Function to display a message box
def display_message():
    messagebox.showinfo("Message", "Hello, GUI!")

# Create the main window
root = tk.Tk()
root.title("Python GUI")

# Create a label widget
label = tk.Label(root, text="Welcome to Python GUI!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=display_message)
button.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a text widget
text = tk.Text(root, height=5, width=30)
text.pack()

# Create a checkbutton widget
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Check Me", variable=check_var)
checkbutton.pack()

# Create a radiobutton widget
radio_var = tk.StringVar(value="Option 1")
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radiobutton1.pack()
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radiobutton2.pack()

# Create a listbox widget
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack()

# Run the application
root.mainloop()
