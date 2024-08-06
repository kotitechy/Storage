import tkinter as tk
import mysql.connector

class stat:
    def widgets(self):
        header_l = tk.Label(self.win, text='SWITERZ BANK',font=('Arial',15,'bold'))
        header_l.place(x=5, y=1)

        self.result_label = tk.Label(self.win, text='',font=('Arial',15,'bold'))
        self.result_label.place(x=1, y=50)

        self.check_authentication()

    def check_authentication(self):

        # Replace these values with your actual database connection details
        host = "localhost"
        user = "root"
        password = "shiva"
        database_name = 'switzbank'

        # Connect to the MySQL server
        connection = mysql.connector.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        try:
            # Execute the SELECT query to check if the entry exists in the 'user' table
            query = "SELECT * FROM authen WHERE sno = 1"
            cursor.execute(query)

            # Fetch the result
            result = cursor.fetchone()
            print('a: ',result[1])
            print('pass: ',result[2])
            query = 'SELECT * FROM users WHERE debit_card_no = %s AND debit_card_pin = %s'
            values = result[1],result[2]
            cursor.execute(query,values)
            res = cursor.fetchone()
            if res:
                self.result_label.config(text='LOGED IN')
            else:
                self.result_label.config(text='NO DATA')
        except mysql.connector.Error as err:
            print(f'Error: {err}')
        finally:
            self.win.after(3000, self.win.destroy)
            # Close the connection
            cursor.close()
            connection.close()

    def __init__(self):
        # Remove the creation of a new Tk() instance here
        self.win = tk.Tk()
        self.win.title('SWITZERBANK-STATS')
        window_width = 200
        window_height = 100
        self.win.geometry(f"{window_width}x{window_height}")
        self.win.resizable(False, False)
        self.widgets()

    def run(self):
        self.win.mainloop()
