import tkinter as tk
import pymysql as sq

class GenAPin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('SWITZERBANK-GENERATE-ATM-PIN')
        window_width = 700
        window_height = 500
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)
        header_label = tk.Label(self.root, text='SWITZ BANK \n GENERATE ATM CARD', font=('Courier', 20, 'bold'))
        header_label.place(x=230, y=10)
        self.widgets()

    def clear_entries(self):
        # Clear the content of all entry widgets
        self.atm_card_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        if hasattr(self, 'pin_entry_1') and hasattr(self, 'pin_entry_2'):
            self.pin_entry_1.delete(0, tk.END)
            self.pin_entry_2.delete(0, tk.END)
    def chk(self):
        try:
            p1 = int(self.pin_entry_1.get())
            p2 = int(self.pin_entry_2.get())
            self.p = p1
            print(self.p)
            if p1 == p2:
                print('PIN MATCHED', self.p)
            else:
                print('PINS UN-MATCHED')
        except Exception as e:
            print(e)

        host = "localhost"
        user = "root"
        password = "root"
        database_name = 'switzbank'

        try:
            with sq.connect(host=host, user=user, password=password, database=database_name) as connection:
                cursor = connection.cursor()

                # Execute the UPDATE query with placeholders
                cursor.execute('SET SQL_SAFE_UPDATES = 0')
                query = "UPDATE users SET debit_card_pin = %s WHERE debit_card_no = %s AND mobile_no = %s"
                values = (self.p, self.atm_card_entry.get(), self.mobile_entry.get())
                cursor.execute(query, values)
                connection.commit()
                self.stat_1.config(text='PIN UPDATED SUCCESS FULLY')
                self.clear_entries()
                print('PIN updated successfully')
        except sq.Error as e:
            print(f"Error: {e}")

    def search_data(self):
        host = "localhost"
        user = "root"
        password = "root"
        database_name = 'switzbank'
        #
        try:
            with sq.connect(host=host, user=user, password=password, database=database_name) as connection:
                cursor = connection.cursor()

                query = "SELECT * FROM users WHERE debit_card_no = %s AND mobile_no = %s"
                values = (self.atm_card_entry.get(), self.mobile_entry.get())
                cursor.execute(query, values)
                result = cursor.fetchone()

                if result:
                    print("DATA found")
                    print(f'name: {result[1]}')
                    self.stats.config(text='DEAR USER\nCREATE YOUR 4 DIGIT PIN FOR ATM')
                    self.check_btn = tk.Button(self.root,text='CHECK', font=('Arial', 10, 'bold', 'italic'), command=self.chk)
                    self.stat_1 = tk.Label(self.root, text='', font=('Arial', 10, 'bold', 'italic'))
                    self.stat_1.place(x=400, y=350)
                    pin_label = tk.Label(self.root, text='4 DIGIT ATM PIN\nUSE ONLY DIGITS', font=('Arial', 12, 'bold', 'italic'))
                    pin_label_1 = tk.Label(self.root, text='4 DIGIT ATM:\n\n\nRE-ENTER PIN:')
                    pin_label.place(x=50, y=300)
                    pin_label_1.place(x=50, y=350)
                    self.pin_entry_1 = tk.Entry(self.root)
                    self.pin_entry_2 = tk.Entry(self.root)
                    self.pin_entry_1.place(x=200, y=350)
                    self.pin_entry_2.place(x=200, y=400)
                    self.check_btn.place(x=250, y=450)

                else:
                    self.stats.config(text='NO USER FOUND\nTRY AGAIN BY CREATING AN ACCOUNT')
        except sq.Error as e:
            print(f"SOMETHING WENT WRONG: {e}")

    def generate_pin(self):
        atm_card_number = self.atm_card_entry.get()
        mobile_number = self.mobile_entry.get()
        print('\n', atm_card_number, '\n', mobile_number)
        self.search_data()

    def widgets(self):
        self.stats = tk.Label(self.root, text='PLEASE FILL THE FOLLOWING AND CONTINUE ', font=('Arial', 12, 'bold', 'italic'))
        self.stats.place(x=150, y=100)

        label = tk.Label(self.root, text='ATM Card Number:')
        label.place(x=50, y=150)

        self.atm_card_entry = tk.Entry(self.root)
        self.atm_card_entry.place(x=200, y=150)

        label = tk.Label(self.root, text='Mobile Number:')
        label.place(x=50, y=200)

        self.mobile_entry = tk.Entry(self.root)
        self.mobile_entry.place(x=200, y=200)

        generate_button = tk.Button(self.root, text='SEARCH', command=self.generate_pin)
        generate_button.place(x=200, y=250)

    def run(self):
        self.root.mainloop()


