import tkinter as tk

import mysql.connector


class ch_bal:
    def cler(self):
        self.atm_card_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    def widgets(self):
        self.atm_card_label = tk.Label(self.root, text='ATM Card Number:')
        self.atm_card_label.place(x=50, y=150)

        self.atm_card_entry = tk.Entry(self.root)
        self.atm_card_entry.place(x=200, y=150)

        self.password_label = tk.Label(self.root, text='Password:')
        self.password_label.place(x=50, y=200)

        self.password_entry = tk.Entry(self.root, show='*')  # Show asterisks for password
        self.password_entry.place(x=200, y=200)

        generate_button = tk.Button(self.root, text='SEARCH',command=self.generate_pin)
        generate_button.place(x=200, y=250)

        header_l = tk.Label(self.root, text='SWITERZ BANK \n USER CHECK-BALANCE', font=('Courier', 20, 'bold'))
        header_l.place(x=210, y=10)

        self.stats = tk.Label(self.root,text='FILL THE DETAILS',font=('Courier', 20, 'bold'))
        self.stats.place(x=200,y=330)


    def authen(self):
        atm_entry = self.atm_card_entry.get()
        pass_entry = self.password_entry.get()

        # Replace these values with your actual database connection details
        host = "localhost"
        user = "root"
        password = "shiva"
        database_name = 'switzbank'

        # Connect to the MySQL server
        connection = mysql.connector.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        try:
            # Execute the SELECT query with placeholders
            query = "SELECT * FROM users WHERE debit_card_no = %s AND debit_card_pin = %s"
            values = (atm_entry, pass_entry)
            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                self.cler()
                print(" User Data: ")
                print(f'NAME: {result[1]}')
                if result[10] == None:
                    print(f'BALANCE: 00000 \nZERO BALANCE')
                    self.stats.config(text='ZERO BALANCE')
                if result[10] == 2000:
                    print(f'BALANCE: {result[10]} \nMINIMUM BALANCE')
                    self.stats.config(text=f'{result[10]} \nMINIMUM BALANCE')
                else:
                    print('BALANCE: ', result[10])
                    self.stats.config(text=f'BALANCE: {result[10]}')

        except:
            print('NO DATA FOUND')

    def generate_pin(self):
        atm_entry = self.atm_card_entry.get()
        pass_entry = self.password_entry.get()
        print('\nATM Card Number:', atm_entry)
        print('Password:', pass_entry)
        self.authen()
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('SWITZERBANK-USER_AUTHENTICATION')
        window_width = 700
        window_height = 500
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)
        self.widgets()

    def run(self):
        self.root.mainloop()
