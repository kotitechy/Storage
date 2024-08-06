import tkinter as tk
import pymysql as sql

import stats


class Authen:
    def sat(self):
        au = stats.stat()
        au.run()

    def cler(self):
        self.atm_card_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def widgets(self):
        self.atm_card_label = tk.Label(self.win, text='ATM Card Number:')
        self.atm_card_label.place(x=50, y=150)

        self.atm_card_entry = tk.Entry(self.win)
        self.atm_card_entry.place(x=200, y=150)

        self.password_label = tk.Label(self.win, text='Password:')
        self.password_label.place(x=50, y=200)

        self.password_entry = tk.Entry(self.win, show='*')  # Show asterisks for the password
        self.password_entry.place(x=200, y=200)

        generate_button = tk.Button(self.win, text='SEARCH', command=self.generate_pin)
        generate_button.place(x=200, y=250)

        header_l = tk.Label(self.win, text='SWITERZ BANK \n USER AUTHENTICATION', font=('Courier', 20, 'bold'))
        header_l.place(x=210, y=10)

        self.stats = tk.Label(self.win, text='FILL THE DETAILS', font=('Courier', 20, 'bold'))
        self.stats.place(x=200, y=330)

    def authen(self):
        atm_entry = self.atm_card_entry.get()
        pass_entry = self.password_entry.get()

        # Replace these values with your actual database connection details
        host = "localhost"
        user = "root"
        password = "root"
        database_name = 'switzbank'

        # Connect to the MySQL server
        connection = sql.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        try:
            # Execute the INSERT query without a WHERE clause
            query = "UPDATE authen SET atm_no = %s, pass = %s WHERE sno = 1"
            values = (atm_entry, pass_entry)
            cursor.execute(query, values)
            print('Data inserted successfully')
        except sql.Error as err:
            print(f'Error: {err}')

        # Commit the transaction and close the connection
        connection.commit()
        cursor.close()
        connection.close()

    def generate_pin(self):
        atm_entry = self.atm_card_entry.get()
        pass_entry = self.password_entry.get()
        print('\nATM Card Number:', atm_entry)
        print('Password:', pass_entry)
        self.authen()
        self.win.destroy()
        self.sat()

    def __init__(self):
        # Remove the creation of a new Tk() instance here
        self.win = tk.Tk()
        self.win.title('SWITZERBANK-USER_AUTHENTICATION')
        window_width = 700
        window_height = 500
        self.win.geometry(f"{window_width}x{window_height}")
        self.win.resizable(False, False)
        self.widgets()

    def run(self):
        self.win.mainloop()

a = Authen()
a.run()
