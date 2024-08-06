import tkinter as tk
from tkinter import Entry, Label, StringVar
import pymysql

def on_submit():
    entered_username = username_var.get()
    entered_password = password_var.get()
    entered_email = email_var.get()

    try:
        # Create a connection to the MySQL server
        db = pymysql.connect(host="localhost", user="root", password="shiva", database="ellenki_college")
        cur = db.cursor()
        print("Connected to MySQL server successfully!")

        # Construct the SELECT query with conditions
        query = "SELECT * FROM stu_regs WHERE full_name = %s AND email = %s AND passwd = %s"
        values = (entered_username, entered_email, entered_password)

        # Execute the SELECT query with conditions
        cur.execute(query, values)

        # Fetch the results
        results = cur.fetchall()

        # Clear the result_label
        result_label.config(text="")

        if results:
            print("Data found:")
            result_label.config(text="Login Success\n Data is")
            for row in results:
                res_label.config(text=row)
                
                print(row)
        else:
            print("No matching data found")
            result_label.config(text="Login Failed \n No such data found \n")

    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        db.close()


def close_window():
    root.destroy()




# Create the main window
root = tk.Tk()
root.title("Student Registration Form")
root.configure(bg="lightblue")
root.resizable(False, False)
# Set the window's width and height
window_width = 400
window_height = 700
root.geometry(f"{window_width}x{window_height}")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for centering the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window's position to center it on the screen
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label for email with some padding
custom_font = ("Arial", 28, "bold italic")
wel_label = Label(root, text="Student Login Page", font=custom_font)
wel_label.pack(pady=5)
custom_font = ("Arial", 15, "bold ")
# Create a label for username with some padding
username_label = Label(root, text="Full Name:", font=custom_font)
username_label.pack(pady=5)

# Create an entry widget for username
username_var = StringVar()
username_entry = Entry(root, textvariable=username_var)
username_entry.pack(pady=5)

# Create a label for email with some padding
email_label = Label(root, text="Email:", font=custom_font)
email_label.pack(pady=5)

# Create an entry widget for email
email_var = StringVar()
email_entry = Entry(root, textvariable=email_var)
email_entry.pack(pady=5)

# Create a label for password with some padding
password_label = Label(root, text="Password:", font=custom_font)
password_label.pack(pady=5)

# Create an entry widget for password (passwords are hidden)
password_var = StringVar()
password_entry = Entry(root, textvariable=password_var, show='*')
password_entry.pack(pady=5)

# Create a button to submit the input
submit_button = tk.Button(root, text="Search", command=on_submit)
submit_button.pack(pady=10)

# close Button
button_cls = tk.Button(root, text="Exit", command=close_window)
button_cls.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", font=custom_font)
result_label.pack()
#results
res_label = tk.Label(root, text="")
res_label.pack()

# Start the main loop for the main window
root.mainloop()

