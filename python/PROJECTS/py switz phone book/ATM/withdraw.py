import tkinter as tk
from tkinter import END

import pymysql as sql


class withdraw:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('SWITZERBANK-GENERATE-ATM-PIN')
        window_width = 700
        window_height = 500
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)
        header_label = tk.Label(self.root, text='SWITZ BANK \n USER_WITHDRAWAL', font=('Courier', 20, 'bold'))
        header_label.place(x=230, y=10)
        self.widgets()
    def des(self):
        self.atm_no.delete(0,END)
        self.pass_en.delete(0,END)
        self.am_1.delete(0,END)
        self.am_2.delete(0,END)
    def depo(self):
        self.stats.config(text='PROCESSING')
        self.am1 = float(self.am_1.get())
        self.am2 = float(self.am_2.get())
        am = self.am2
        if self.am1 == self.am2:
            print('amount matched')
            host = "localhost"
            user = "root"
            password = "root"
            database_name = 'switzbank'

            try:
                with sql.connect(host=host, user=user, password=password,
                                             database=database_name) as connection:
                    cursor = connection.cursor()

                    query = "SELECT * FROM users WHERE debit_card_no = %s AND debit_card_pin = %s"
                    values = (self.atm_n, self.pass_n)
                    cursor.execute(query, values)
                    result = cursor.fetchone()
                    print(result[10])

                    if result:
                        print("DATA found")
                        print(f'name: {result[1]}')
                        self.stats.config(text='USER FOUND')

                        if am < 500:
                            print("MINIMUM AMOUNT SHOULD BE 500 ")
                        elif am > 100000:
                            print("DAY LIMIT IS 1LAKH")
                        else:
                            if result[10] < am :
                                print('insufficient balance')
                                self.stats.config(text='insufficient balance')

                            elif am > result[10]:
                                print('insufficient balance')
                                self.stats.config(text='insufficient balance')
                            else :
                                rem = float(result[10]) - am
                                print(rem)
                                print('bal : ',rem)
                                cursor.execute('SET SQL_SAFE_UPDATES = 0')
                                query = "UPDATE users SET amount = %s WHERE debit_card_no = %s AND debit_card_pin = %s"
                                values = (rem, self.atm_n,self.pass_n)
                                cursor.execute(query, values)
                                connection.commit()
                                self.stats.config(text=f'BAL : {rem}')
                                self.root.after(2000, self.stats.config(text=f'AMOUNT WITHDRAWED SUCCESSFULLY {am} BAL {rem}'))
                                self.des()

                                print("Amount updated successfully")
                            print('bal : ',result[10])

                    else:
                        self.stats.config(text='NO USER FOUND\nTRY AGAIN BY CREATING AN ACCOUNT')
            except sql.Error as e:
                print(f"SOMETHING WENT WRONG: {e}")
        else:
            print('ENTER A VALID AMOUNT / CHECK ENTERED ONE')

        pass

    def srh(self, a, b):
        host = "localhost"
        user = "root"
        password = "root"
        database_name = 'switzbank'

        try:
            with sql.connect(host=host, user=user, password=password, database=database_name) as connection:
                cursor = connection.cursor()

                query = "SELECT * FROM users WHERE debit_card_no = %s AND debit_card_pin = %s"
                values = (a, b)
                cursor.execute(query, values)
                result = cursor.fetchone()
                print(result)

                if result:
                    print("DATA found")
                    print(f'name: {result[1]}')
                    self.stats.config(text='ENTER WITHDRAWAL AMOUNT')

                    self.check_btn = tk.Button(self.root, text='CHECK', font=('Arial', 10, 'bold', 'italic'),command=self.depo)
                    self.stat_1 = tk.Label(self.root, text='', font=('Arial', 10, 'bold', 'italic'))
                    self.stat_1.place(x=400, y=350)

                    pin_label = tk.Label(self.root, text='ENTER AMOUNT FOR WITHDRAWAL : ',
                                         font=('Arial', 12, 'bold', 'italic'))
                    pin_label_1 = tk.Label(self.root, text='ENTER AMOUNT : ')
                    pin_label_2 = tk.Label(self.root, text='RE-ENTER AMOUNT : ')
                    pin_label.place(x=50, y=300)
                    pin_label_1.place(x=50, y=350)
                    pin_label_2.place(x=50, y=400)

                    self.am_1 = tk.Entry(self.root)
                    self.am_2 = tk.Entry(self.root)
                    self.am_1.place(x=200, y=350)
                    self.am_2.place(x=200, y=400)
                    self.check_btn.place(x=250, y=450)

                else:
                    self.stats.config(text='NO USER FOUND\nTRY AGAIN BY CREATING AN ACCOUNT')
        except sql.Error as e:
            print(f"SOMETHING WENT WRONG: {e}")

    def search(self):
        self.atm_n = self.atm_no.get()
        self.pass_n = self.pass_en.get()
        self.srh(self.atm_n, self.pass_n)

    def widgets(self):
        self.stats = tk.Label(self.root, text='PLEASE FILL THE FOLLOWING AND CONTINUE ',
                              font=('Arial', 12, 'bold', 'italic'))
        self.stats.place(x=150, y=100)

        label = tk.Label(self.root, text='ATM Card Number:')
        label.place(x=50, y=150)

        self.atm_no = tk.Entry(self.root)
        self.atm_no.place(x=200, y=150)

        label = tk.Label(self.root, text='PASSWORD :')
        label.place(x=50, y=200)

        self.pass_en = tk.Entry(self.root)
        self.pass_en.place(x=200, y=200)

        generate_button = tk.Button(self.root, text='SEARCH', command=self.search)
        generate_button.place(x=200, y=250)

    def run(self):
        self.root.mainloop()



