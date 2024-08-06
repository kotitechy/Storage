import tkinter as tk
from tkinter import Entry, Label, StringVar
import pymysql

class regs:
    def regs(self):
        pass
def on_submit():
    entered_username = username_var.get()
    entered_password = password_var.get()
    entered_email = email_var.get()

    try:
        # Create a connection to the MySQL server
        db = pymysql.connect(host="localhost", user="root", password="shiva", database="ellenki_college")
        cur = db.cursor()
        print("Connected to MySQL server successfully!")

        # Insert data into the database using parameterized query
        query = "INSERT INTO stu_regs (full_name, email, passwd) VALUES (%s, %s, %s)"
        values = (entered_username, entered_email, entered_password)
        cur.execute(query, values)
        status_label = Label(root, text="Student Success Fully Registered \n name : "+entered_username+" \n email : "+entered_email+" \n Password : "+entered_password)
        status_label.pack()

        # Commit the changes to the database
        db.commit()

        print("Inserted Successfully")

    except pymysql.Error as e:
        print(f"Error: {e}")
        # Rollback changes in case of error
        db.rollback()
    finally:
        # Close the database connection
        db.close()
#reset inputs
def on_reset():
    username_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")

# Create a label for username
username_label = Label(root, text="Full Name:")
username_label.pack()

# Create an entry widget for username
username_var = StringVar()
username_entry = Entry(root, textvariable=username_var)
username_entry.pack()

# Create a label for email
email_label = Label(root, text="Email:")
email_label.pack()

# Create an entry widget for email
email_var = StringVar()
email_entry = Entry(root, textvariable=email_var)
email_entry.pack()

# Create a label for password
password_label = Label(root, text="Password:")
password_label.pack()

# Create an entry widget for password (passwords are hidden)
password_var = StringVar()
password_entry = Entry(root, textvariable=password_var, show='*')
password_entry.pack()

# Create a button to submit the input
submit_button = tk.Button(root, text="Create Profile", command=on_submit)
submit_button.pack()

# Create a button to reset the input
reset_button = tk.Button(root, text="Reset", command=on_reset)
reset_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
