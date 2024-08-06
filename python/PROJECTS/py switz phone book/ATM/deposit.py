import tkinter as tk

import pymysql as sql

import authen


class Deposit:
    def res(self):
        self.am_entry_1.delete(0,tk.END)
        self.am_entry_1.delete(0,tk.END)
    def widgets(self):
        self.amt_label_1 = tk.Label(self.win, text='AMOUNT HERE:')
        self.amt_label_1.place(x=50, y=150)

        self.am_entry_1 = tk.Entry(self.win)
        self.am_entry_1.place(x=200, y=150)

        self.amt_label_2 = tk.Label(self.win, text='RE-ENTER AMOUNT:')
        self.amt_label_2.place(x=50, y=200)

        self.am_entry_2 = tk.Entry(self.win)  # Show asterisks for the password
        self.am_entry_2.place(x=200, y=200)

        generate_button = tk.Button(self.win, text='DEPOSIT', command=self.check_amount)
        generate_button.place(x=200, y=250)

        header_l = tk.Label(self.win, text='SWITERZ BANK \n USER DEPOSIT', font=('Courier', 20, 'bold'))
        header_l.place(x=210, y=10)

        self.stats = tk.Label(self.win, text='FILL THE DETAILS', font=('Courier', 20, 'bold'))
        self.stats.place(x=100, y=330)

    def check_amount(self):
        amount_1 = self.am_entry_1.get()
        amount_2 = self.am_entry_2.get()

        try:
            amount_1 = float(amount_1)
            amount_2 = float(amount_2)

            if amount_1 == amount_2:
                print("AMOUNT MATCHED \nPROCESSING")
                self.stats.config(text='PROCESSING')
                amount = float(amount_1)
                if amount < 1000:
                    print('PLEASE ENTER AMOUNT GREATER THAN 999')
                    self.stats.config(text='PLEASE ENTER AMOUNT GREATER THAN 999')
                elif amount >=  1000 :
                    print('ok')
                    self.stats.config(text='PROCESSING')
                    # Replace these values with your actual database connection details
                    host = "localhost"
                    user = "root"
                    password = "root"
                    database_name = 'switzbank'

                    # Connect to the MySQL server
                    connection = sql.connect(host=host, user=user, password=password,
                                                         database=database_name)
                    cursor = connection.cursor()
                    connection = sql.connect(host=host, user=user, password=password,
                                                         database=database_name)
                    cursor = connection.cursor()

                    try:
                            query = "SELECT * FROM authen WHERE sno = 1"
                            cursor.execute(query)
                            result = cursor.fetchone()
                            print(result[1],result[2])
                            cursor.execute('SET SQL_SAFE_UPDATES = 0')
                            query_1 = "SELECT * FROM users WHERE debit_card_no = %s AND debit_card_pin = %s"
                            values = (result[1],result[2])
                            cursor.execute(query_1, values)
                            am = cursor.fetchone()
                            print(am)
                            
                            query = "UPDATE users SET amount = %s WHERE debit_card_no = %s AND debit_card_pin = %s"
                            values = (float(amount), result[1],result[2])
                            cursor.execute(query, values)
                            connection.commit()
                            self.win.after(2000, self.stats.config(text=f'AMOUNT DEPOSITED SUCCESSFULLY {amount}'))
                            print("Amount updated successfully")
                    except sql.Error as e:
                        print(f"Error updating the amount: {e}")
                        self.stats.config(text='ERROR UPDATING AMOUNT')

                    finally:
                        # Close the cursor and connection in the final block
                        cursor.close()
                        connection.close()
                elif amount > 1000000:
                    print('MAX AMOUNT IS 1000000 / 10 LAKHS')
                    self.stats.config(text='MAX AMOUNT IS 1000000 / 10 LAKHS')

            else:
                print('AMOUNT IN BOTH FIELDS MUST MATCH')

        except ValueError:
            print('PLEASE ENTER A VALID AMOUNT')

    def generate_pin(self):
        pass

    def __init__(self):

        self.win = tk.Tk()
        self.win.title('SWITZERBANK-USER_DEPOSIT')
        window_width = 700
        window_height = 500
        self.win.geometry(f"{window_width}x{window_height}")
        self.win.resizable(False, False)
        self.widgets()

    def run(self):
        self.win.mainloop()
