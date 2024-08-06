import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk


class Crt_ac:
    def choose_photo(self):
        file_path = filedialog.askopenfilename(title="Select a Photo",
                                               filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            # Load the image and display it
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            with open(file_path, 'rb') as image_file:
                self.prof_data = image_file.read()
                # print(self.prof_data)
            # Update the label with the chosen photo
            self.profile_photo_label.config(width=15, height=10)
            self.profile_photo_label.config(text='ok')
            self.profile_photo_label.image = photo

    def choose_id(self):
        file_path = filedialog.askopenfilename(title="Select a Photo",
                                               filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            # Load the image and display it
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            with open(file_path, 'rb') as image_file:
                self.id_data = image_file.read()
                # print(self.id_data)
            # Update the label with the chosen photo
            self.id_proof_photo_label.config(width=15, height=10)
            self.id_proof_photo_label.config(text='ok')
            self.id_proof_photo_label.image = photo

    def __init__(self):
        self.win = tk.Tk()
        self.win.title('ACCOUNT CREATION SWITZER BANK')
        self.win.geometry('800x600')
        self.win.config(bg='light pink')
        self.win.resizable(False, False)

        self.create_widgets()

        # Clear button
        clear_button = tk.Button(self.win, text="Clear Entries", command=self.clear_entries, bg='light yellow')
        clear_button.place(x=350, y=500)

    def clear_entries(self):
        # Clear text in all entry widgets
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.sur_name_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.add_entry.delete(0, tk.END)
        self.qualification_entry.delete(0, tk.END)
        self.mobil_no_entry.delete(0, tk.END)
        self.adhar_no_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)  # Added
        self.pancard_entry.delete(0, tk.END)  # Added
        self.gender_var.set("Male")  # Reset gender to default
        self.account_type_combobox.set("Major")  # Reset account type to default

        # Clear the result label
        # self.result_label.config(text="")

        # Clear profile and ID proof photos
        self.profile_photo_label.config(image="")
        self.id_proof_photo_label.config(image="")

        self.profile_photo_label.config(width=15, height=10)
        self.id_proof_photo_label.config(width=15, height=10)

    def create_widgets(self):
        # Header
        header_label = tk.Label(self.win, text="Create Account", font=('Helvetica', 16, 'bold'), bg='light pink')
        header_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        # Entry widgets for personal details
        self.first_name_label = tk.Label(self.win, text="First Name:", bg='light pink')
        self.first_name_label.place(x=10, y=80)

        self.first_name_entry = tk.Entry(self.win)
        self.first_name_entry.place(x=150, y=80)
        self.first_name_entry.insert(0, "Enter your first name")

        self.last_name_label = tk.Label(self.win, text="Last Name:", bg='light pink')
        self.last_name_label.place(x=10, y=110)

        self.last_name_entry = tk.Entry(self.win)
        self.last_name_entry.place(x=150, y=110)
        self.last_name_entry.insert(0, "Enter your last name")

        self.sur_name_label = tk.Label(self.win, text="Surname:", bg='light pink')
        self.sur_name_label.place(x=10, y=140)

        self.sur_name_entry = tk.Entry(self.win)
        self.sur_name_entry.place(x=150, y=140)
        self.sur_name_entry.insert(0, "Enter your surname")

        self.dob_label = tk.Label(self.win, text="Date of Birth:", bg='light pink')
        self.dob_label.place(x=10, y=170)

        self.dob_entry = tk.Entry(self.win)
        self.dob_entry.place(x=150, y=170)
        self.dob_entry.insert(0, "Enter your date of birth (YYYY-MM-DD)")

        # Entry widgets for additional details
        self.add_label = tk.Label(self.win, text="Address:", bg='light pink')
        self.add_label.place(x=10, y=200)

        self.add_entry = tk.Entry(self.win)
        self.add_entry.place(x=150, y=200)
        self.add_entry.insert(0, "Enter your address")

        self.qualification_label = tk.Label(self.win, text="Qualification:", bg='light pink')
        self.qualification_label.place(x=10, y=230)

        self.qualification_entry = tk.Entry(self.win)
        self.qualification_entry.place(x=150, y=230)
        self.qualification_entry.insert(0, "Enter your qualification")

        self.mobil_no_label = tk.Label(self.win, text="Mobile Number:", bg='light pink')
        self.mobil_no_label.place(x=10, y=260)

        self.mobil_no_entry = tk.Entry(self.win)
        self.mobil_no_entry.place(x=150, y=260)
        self.mobil_no_entry.insert(0, "Enter your mobile number")

        self.adhar_no_label = tk.Label(self.win, text="Adhar Number:", bg='light pink')
        self.adhar_no_label.place(x=10, y=290)

        self.adhar_no_entry = tk.Entry(self.win)
        self.adhar_no_entry.place(x=150, y=290)
        self.adhar_no_entry.insert(0, "Enter your Aadhar number")

        # Radiobuttons for gender selection
        self.gender_label = tk.Label(self.win, text="Gender:", bg='light pink')
        self.gender_label.place(x=10, y=320)

        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")  # Default value

        self.gender_male = tk.Radiobutton(self.win, text="Male", variable=self.gender_var, value="Male",
                                          bg='light pink')
        self.gender_male.place(x=150, y=320)

        self.gender_female = tk.Radiobutton(self.win, text="Female", variable=self.gender_var, value="Female",
                                            bg='light pink')
        self.gender_female.place(x=250, y=320)

        self.gender_others = tk.Radiobutton(self.win, text="Others", variable=self.gender_var, value="Others",
                                            bg='light pink')
        self.gender_others.place(x=350, y=320)

        # Combobox for account type
        self.account_type_label = tk.Label(self.win, text="Account Type:", bg='light pink')
        self.account_type_label.place(x=10, y=350)

        self.account_type_var = tk.StringVar()
        account_type_values = ["Major", "Minor"]
        self.account_type_combobox = ttk.Combobox(self.win, textvariable=self.account_type_var,
                                                  values=account_type_values)
        self.account_type_combobox.place(x=150, y=350)
        self.account_type_combobox.set("Major")  # Default value
        self.email_label = tk.Label(self.win, text="Email:", bg='light pink')
        self.email_label.place(x=10, y=380)

        self.email_entry = tk.Entry(self.win)
        self.email_entry.place(x=150, y=380)
        self.email_entry.insert(0, "Enter your email")

        self.pancard_label = tk.Label(self.win, text="Pancard Number:", bg='light pink')
        self.pancard_label.place(x=10, y=410)

        self.pancard_entry = tk.Entry(self.win)
        self.pancard_entry.place(x=150, y=410)
        self.pancard_entry.insert(0, "Enter your Pancard number")

        # Submit button
        submit_button = tk.Button(self.win, text="Submit", command=self.onsubmit, bg='light blue')
        submit_button.place(x=250, y=500)

        # # Result label
        # self.result_label = tk.Label(self.win, text="", bg='light pink')
        # self.result_label.place(x=10, y=430)

        # Choose profile photo button
        choose_profile_button = tk.Button(self.win, text="Choose Profile Photo", command=self.choose_photo,
                                          bg='light yellow')
        choose_profile_button.place(x=350, y=250)

        # Display profile photo
        self.profile_photo_label = tk.Label(self.win, text="Profile Photo", bg='white', width=20, height=12)
        self.profile_photo_label.place(x=350, y=50)

        # Choose ID proof photo button
        choose_id_proof_button = tk.Button(self.win, text="Choose ID Proof Photo", command=self.choose_id,
                                           bg='light yellow')
        choose_id_proof_button.place(x=600, y=250)

        # Display ID proof photo
        self.id_proof_photo_label = tk.Label(self.win, text="ID Proof Photo", bg='white', width=20, height=12)
        self.id_proof_photo_label.place(x=600, y=50)
        # clearing entries
        self.clear_entries()

    def onsubmit(self):
        # ... (previous code remains unchanged)

        import mysql.connector

        # Replace these values with your actual database connection details
        host = "192.168.23.173"
        user = "root"
        password = "root"
        database_name = 'switzbank'

        try:
            # Connect to the MySQL server
            connection = mysql.connector.connect(host=host, user=user, password=password, database=database_name)
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Execute the INSERT query with placeholders
            query = "INSERT INTO USERS (user_name, dob, gender, address, qualification, mobile_no, adhar_no, email, acc_type, prof_img, id_proof) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (user_name, dob, gender, address, qualification, mobile_number, adhar_number, email, account_type,
                      self.prof_data, self.id_data)
            cursor.execute(query, values)
            print('DATA INSERTED SUCCESSFULLY')
        except mysql.connector.Error as err:
            print(f'FAILED TO INSERT DATA: {err}')
        finally:
            # Commit the changes and close the connection
            connection.commit()
            cursor.close()
            connection.close()

        # Clear entries and photos after submission
        self.clear_entries()


    def onsubmit(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        sur_name = self.sur_name_entry.get()
        user_name = first_name+last_name+sur_name
        dob = self.dob_entry.get()
        address = self.add_entry.get()
        qualification = self.qualification_entry.get()
        mobile_number = self.mobil_no_entry.get()
        adhar_number = self.adhar_no_entry.get()
        gender = self.gender_var.get()
        account_type = self.account_type_var.get()
        email = self.email_entry.get()
        pancard_number = self.pancard_entry.get()
        print(first_name, last_name, sur_name, '\n', dob, '\n', address, '\n', qualification, '\n', mobile_number, '\n',adhar_number, '\n', gender, '\n', account_type, '\n', email, '\n', pancard_number)
        print(self.prof_data, '\n', self.id_data)
        self.clear_entries()

        import pymysql

        # Replace these values with your actual database connection details
        host = "192.168.23.173"
        user = "root"
        password = "root"
        database_name = 'switzbank'

        # Connect to the MySQL server
        connection = pymysql.connect(host=host, user=user, password=password)
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        try:
            # Connect to the MySQL server
            connection = pymysql.connect(host="localhost", user="root", password="shiva", database='switzbank')
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            # Execute the INSERT query with placeholders
            query = "INSERT INTO USERS (user_name, dob, gender, address, qualification, mobile_no, adhar_no, email, acc_type,prof_img,id_proof) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (user_name, dob, gender, address, qualification, mobile_number, adhar_number, email, account_type,self.prof_data,self.id_data)
            cursor.execute(query, values)
            print('DATA INSERTED SUCCESSFULLY')
        except pymysql.connector.Error as err:
            print(f'FAILED TO INSERT DATA: {err}')
        finally:
            # Commit the changes and close the connection
            connection.commit()
            cursor.close()
            connection.close()

        # Clear entries and photos after submission
        self.clear_entries()
    def run(self):
        self.win.mainloop()

