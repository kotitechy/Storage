import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Background Image")

# Load the background image using Pillow
background_image = Image.open("forest.jpg")

# Convert the background image to a PhotoImage object
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas widget to display the background image
canvas = tk.Canvas(root, width=background_image.width(), height=background_image.height())
canvas.pack()

# Display the background image on the Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# You can add other widgets on top of the Canvas, such as labels, buttons, etc.
label = tk.Label(root, text="Hello, World!", bg="white")
label.pack()

# Run the Tkinter main loop
root.mainloop()
