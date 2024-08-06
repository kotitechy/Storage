import tkinter as tk
from tkinter import PhotoImage

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Window with Image Background")

# Set the initial size of the window to 700x500 pixels
window_width, window_height = 700, 500

# Center the window on the screen
center_window(root, window_width, window_height)

# Disable resizing of the window
root.resizable(False, False)

# Make the window non-movable
# root.overrideredirect(True)
# Load the image file
image_path = "bg_image.png"
bg_image = PhotoImage(file=image_path)

# Create a canvas widget to display the image
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Create a label widget on top of the canvas
label = tk.Label(root, text="KUMMARI \n SHIVACHARAN ", font=("Comic Sans MS", 22, "italic","bold"), fg="LightBlue")
label.place(x=450, y=100)

# Make the label background transparent
label.configure(bg=root.cget("bg"))

# Make the label background transparent
label.configure(bg=root.cget("bg"))

# Run the Tkinter event loop
root.mainloop()
