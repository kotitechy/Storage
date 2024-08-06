import tkinter as tk
from tkinter import Entry, Label, StringVar
import pymysql

def on_submit():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Connect to the MySQL database
    db = pymysql.connect(host="localhost", user="root", passwd="shiva", database="shivdb")

    # Create a cursor object
    cursor = db.cursor()

    # Define an SQL INSERT statement
    insert_query = "INSERT INTO student (name, college) VALUES (%s, %s)"
    data = (entered_username, entered_password)

    # Execute the INSERT statement
    cursor.execute(insert_query, data)
    
    # Commit the changes to the database
    db.commit()

    # Close the database connection
    db.close()
    
    result_label.config(text="Data inserted successfully!")

# Create the main window
root = tk.Tk()
root.title("Username and Password Input")

# Create a label for username
username_label = Label(root, text="Username:")
username_label.pack()

# Create an entry widget for username
username_var = StringVar()
username_entry = Entry(root, textvariable=username_var)
username_entry.pack()

# Create a label for password
password_label = Label(root, text="Password:")
password_label.pack()

# Create an entry widget for password (passwords are hidden)
password_var = StringVar()
password_entry = Entry(root, textvariable=password_var, show='*')
password_entry.pack()

# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
