import tkinter as tk
from datetime import datetime

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def submit_form():
    # Get values from entry widgets
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    age = age_entry.get()
    address = address_entry.get()
    study = study_entry.get()
    relation = relation_entry.get()
    dob = dob_entry.get()

    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print values
    print('Name:', name)
    print('Email:', email)
    print('Phone:', phone)
    print('Gender:', gender)
    print('Age:', age)
    print('Address:', address)
    print('Study:', study)
    print('Relation:', relation)
    print('Date of Birth:', dob)
    print('Timestamp:', timestamp)

    # Write data to a text file
    with open("collected_data.txt", "a") as file:
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Study: {study}\n")
        file.write(f"Relation: {relation}\n")
        file.write(f"Date of Birth: {dob}\n")
        file.write("\n")

    # Update result label
    result_label.config(text="Data submitted and saved to 'collected_data.txt'")

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Extended Form")

# Set the initial size of the window to 700x500 pixels
window_width, window_height = 700, 500

# Center the window on the screen
center_window(root, window_width, window_height)

# Disable resizing of the window
root.resizable(False, False)

# Create a header label
header_label = tk.Label(root, text="Welcome", font=('Arial', 20))
header_label.place(relx=0.5, rely=0.05, anchor='center')

# Create and place entry widgets with decorated styles
entry_width = 25
entry_font = ('Arial', 10, 'italic')

tk.Label(root, text="Name:").place(x=50, y=50)
name_entry = tk.Entry(root, width=entry_width, font=entry_font)
name_entry.place(x=150, y=50)

tk.Label(root, text="Email:").place(x=50, y=80)
email_entry = tk.Entry(root, width=entry_width, font=entry_font)
email_entry.place(x=150, y=80)

tk.Label(root, text="Phone:").place(x=50, y=110)
phone_entry = tk.Entry(root, width=entry_width, font=entry_font)
phone_entry.place(x=150, y=110)

tk.Label(root, text="Gender:").place(x=50, y=140)
gender_var = tk.StringVar()
gender_var.set("Male")
gender_menu = tk.OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_menu.place(x=150, y=140)

tk.Label(root, text="Age:").place(x=50, y=170)
age_entry = tk.Entry(root, width=entry_width, font=entry_font)
age_entry.place(x=150, y=170)

tk.Label(root, text="Address:").place(x=50, y=200)
address_entry = tk.Entry(root, width=entry_width, font=entry_font)
address_entry.place(x=150, y=200)

tk.Label(root, text="Study:").place(x=50, y=230)
study_entry = tk.Entry(root, width=entry_width, font=entry_font)
study_entry.place(x=150, y=230)

tk.Label(root, text="Relation:").place(x=50, y=260)
relation_entry = tk.Entry(root, width=entry_width, font=entry_font)
relation_entry.place(x=150, y=260)

tk.Label(root, text="Date of Birth:").place(x=50, y=290)
dob_entry = tk.Entry(root, width=entry_width, font=entry_font)
dob_entry.place(x=150, y=290)

# Create and place submit button with decorated style
submit_button = tk.Button(root, text="Submit", command=submit_form, bg='purple', fg='white', font=('Arial', 12))
submit_button.place(x=50, y=320)

# Create a label to display the entered values
result_label = tk.Label(root, text="Submit the form to see results", bg='white')
result_label.place(x=50, y=350)

# Run the Tkinter event loop
root.mainloop()
