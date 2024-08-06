import pymysql as sq
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageGrab
from reportlab.pdfgen import canvas


class UpdateDetails:

    def print_to_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if file_path:
            # Grab the content of the Tkinter window as an image
            window = self.win1
            x = window.winfo_rootx()
            y = window.winfo_rooty()
            width = window.winfo_width()
            height = window.winfo_height()
            image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

            # Convert the image to PDF using reportlab
            pdf_path = file_path
            pdf_canvas = canvas.Canvas(pdf_path)
            pdf_canvas.drawInlineImage(image, 0, 0)
            pdf_canvas.save()

            print(f"Window content saved as PDF: {pdf_path}")
    def fetch_data(self):
        mobile_no = self.mobile_entry.get()
        adhar_no = self.adhar_entry.get()

        # Replace these values with your actual database connection details
        host = "localhost"
        user = "root"
        password = "root"
        database_name = 'switzbank'

        # Connect to the MySQL server
        connection = sq.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        try:
            # Execute the SELECT query with placeholders
            query = "SELECT * FROM users WHERE mobile_no = %s AND adhar_no = %s"
            values = (mobile_no, adhar_no)
            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                print(f"User with mobile_no {mobile_no} and adhar_no {adhar_no} found. User Data: ")
                print(f'name: {result[0]}')
                self.stats.config(text='USER FOUND \n GENERATING DEBIT_CARD')

                debit_no = "SWTZ" + str(result[0]) + "KZ"
                try:
                    # Execute the UPDATE query with placeholders
                    query = "UPDATE users SET debit_card_no = %s WHERE mobile_no = %s"
                    values = (debit_no, mobile_no)
                    cursor.execute(query, values)

                    today = datetime.now()
                    dob = result[2]
                    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                    print('age : ', age)

                    if age >= 18:
                        cursor.execute("UPDATE users SET acc_type = 'major' WHERE mobile_no = %s AND adhar_no = %s", (mobile_no, adhar_no))
                    else:
                        cursor.execute("UPDATE users SET acc_type = 'minor' WHERE mobile_no = %s AND adhar_no = %s", (mobile_no, adhar_no))

                    connection.commit()
                    print("SUCCESSFULLY UPDATED THE DATA")
                    self.stats.config(text='YOUR DEBIT_CARD HAS BEEN GENERATED')
                except sq.Error as update_err:
                    print(f'FAILED TO UPDATE DATA: {update_err}')
                    self.stats.config(text='USER NOT FOUND \n PLEASE CREATE AN ACCOUNT FIRST ')

                self.win1 = tk.Tk()
                self.win1.title('ATM/DEBIT_CARD SWITZ-BANK')
                self.win1.geometry('500x300')
                self.win1.resizable(False, False)
                self.win1.config(background='orange')
                try:
                    # Execute the SELECT query with placeholders
                    query = "SELECT * FROM users WHERE mobile_no = %s AND adhar_no = %s"
                    values = (mobile_no, adhar_no)
                    cursor.execute(query, values)
                    result = cursor.fetchone()
                finally:
                    connection.close()
                    cursor.close()
                header = tk.Label(self.win1, text="SWITZ BANK \n DEBIT CARD", font=('Arial', 18), bg='orange')
                header.place(x=150, y=10)

                rupay = tk.Label(self.win1, text="RUPAY", font=('Arial', 20, 'bold', 'italic'), bg='orange')
                rupay.place(x=300, y=250)

                gld_plat = tk.Label(self.win1, text='-|-|-|-|- \n -|-|-|-|- \n -|-|-|-|- \n -|-|-|-|-', bg='#FFD700', width=5, height=3)
                gld_plat.place(x=400, y=80)

                name_label = tk.Label(self.win1, text="Name:", font=('Arial', 12), bg='orange')
                name_label.place(x=10, y=100)

                acno_label = tk.Label(self.win1, text="AC_NO: \n\n AC: \n\n\n CVV 2398 \n\nEXP : 04/27", font=('Arial', 12), bg='orange')
                acno_label.place(x=10, y=150)

                name_value_label = tk.Label(self.win1, text=f"{result[1]}", font=('Arial', 12), bg='orange')
                name_value_label.place(x=150, y=100)

                s = result[11]
                formatted_s = "     ".join([s[i:i + 4] for i in range(0, len(s), 4)])
                print(formatted_s)
                acno_value_label = tk.Label(self.win1, text=formatted_s + f'\n\n {result[9]}', font=('Arial', 12), bg='orange')
                acno_value_label.place(x=150, y=150)

                print_button = tk.Button(self.root, text="Print to PDF", font=('Arial', 12), bg='light green', width=12,
                                         height=1, command=self.print_to_pdf)
                print_button.grid(row=3, column=0, columnspan=2, pady=10)
                print_button.place(x=300, y=350)
                self.win1.mainloop()
            else:
                print("User not found.")
                self.stats.config(text='USER NOT FOUND \n PLEASE CREATE AN ACCOUNT FIRST ')
        except mysql.connector.Error as err:
            print(f'FAILED TO EXECUTE QUERY: {err}')
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def des(self):
        self.root.destroy()
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('SWITERZBANK-GENERATE-ATM-CARD')
        window_width = 700
        window_height = 500
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)

        header_l = tk.Label(self.root, text='SWITZ BANK \n GENERATE ATM CARD', font=('Courier', 20, 'bold'))
        header_l.place(x=230, y=10)

        mobile_label = tk.Label(self.root, text="Mobile Number:")
        mobile_label.grid(row=0, column=0, padx=10, pady=10)
        mobile_label.place(x=10, y=150)

        adhar_label = tk.Label(self.root, text="Aadhar Number:")
        adhar_label.grid(row=1, column=0, padx=10, pady=10)
        adhar_label.place(x=10, y=200)

        self.mobile_entry = tk.Entry(self.root)
        self.mobile_entry.grid(row=0, column=1, padx=10, pady=10)
        self.mobile_entry.place(x=130, y=150)

        self.adhar_entry = tk.Entry(self.root)
        self.adhar_entry.grid(row=1, column=1, padx=10, pady=10)
        self.adhar_entry.place(x=130, y=200)

        submit_button = tk.Button(self.root, text="Submit", font=('Arial', 12), bg='light blue', width=10, height=1, command=self.fetch_data)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)
        submit_button.place(x=140, y=250)
        b8 = tk.Button(self.root, text='EXIT', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.des)
        b8.place(x=250, y=400)

        self.stats = tk.Label(self.root, text='PLEASE FILL ALL COLUMNS', font=('Arial', 13, 'bold'))
        self.stats.place(x=300, y=250)

        self.root.mainloop()


