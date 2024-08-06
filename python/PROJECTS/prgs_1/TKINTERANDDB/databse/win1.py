import tkinter as tk

def submit():
    student_name = name_entry.get()
    college_name = college_entry.get()
    display_label.config(text=f"Student Name: {student_name}\nCollege: {college_name}")

# Create the main application window
app = tk.Tk()
app.title("Student Information")

# Create and place widgets (labels, entry fields, button)
name_label = tk.Label(app, text="Student Name:")
name_label.pack()

name_entry = tk.Entry(app)
name_entry.pack()

college_label = tk.Label(app, text="College:")
college_label.pack()

college_entry = tk.Entry(app)
college_entry.pack()

submit_button = tk.Button(app, text="Submit", command=submit)
submit_button.pack()

display_label = tk.Label(app, text="", wraplength=200)
display_label.pack()

# Start the GUI main loop
app.mainloop()
