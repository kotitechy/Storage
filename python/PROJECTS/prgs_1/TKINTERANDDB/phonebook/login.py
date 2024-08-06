import tkinter as tk
from tkinter import messagebox

import mysql.connector

from main import main_win
from signin import sin


class log():

    def clk(self):
        n = self.usr.get()
        p = self.passw.get()
        print("Values :", n, " , ", p)

        try:
            # Use a context manager to ensure proper handling of the connection
            with mysql.connector.connect(host='192.168.23.173', user='root', passwd='root', database='phonebook') as db:
                with db.cursor() as cur:
                    print('Successfully connected to db')
                    try:

                        cur.execute('SELECT * FROM usr_table WHERE name = %s', (n,))
                        r = cur.fetchone()
                        if r:
                            nl = r[1]
                            print(nl)
                            cur.execute(f'UPDATE cache SET name = %s WHERE sno = 1', (n,))
                            db.commit()
                            print('cached data', n, p)

                            if r[1] == n:
                                print('Login')
                                c = main_win()
                                c.usr_n = n
                                self.stat.config(text="Login Success")
                                messagebox.showerror("Success", "Login Success")
                                self.root.destroy()
                                c.mai(n)

                            else:
                                print('Login Failed')
                                self.stat.config(text='No user found')


                        else:
                            print('User not found')
                            messagebox.showerror("Error", "Login Failed")

                    except mysql.connector.Error as e:
                        print(f'Error executing query: {e}')

        except mysql.connector.Error as e:
            print(f'Failed to connect to db: {e}')

    def login(self):
        self.root = tk.Tk()
        self.root.title('Login')
        self.root.geometry('300x300')

        self.usr = tk.Entry(self.root)
        self.passw = tk.Entry(self.root)
        self.usr.place(x=100, y=100)
        self.passw.place(x=100, y=150)

        self.stat = tk.Label(self.root,text='')
        self.stat.place(x=200,y=30)

        usr_l = tk.Label(self.root, text='Enter Email')
        passw_l = tk.Label(self.root, text='Enter Passwd')
        usr_l.place(x=10, y=100)
        passw_l.place(x=10, y=150)

        con = tk.Button(self.root, text='Login', command=self.clk)
        con.place(x=100, y=200)

        self.root.mainloop()


'''
        try:
            db = mysql.connector.connect(host='localhost', user='root', passwd='root')
            cur = db.cursor()
            print('Successfully connected to db')
            try:
                cur.execute('use phonebook')
                db.commit()
                # Assuming `cur` is your cursor object
                cur.execute('show tables')
                r = cur.fetchall()
                print(r)

                for i in r:
                    if i.lower() == n:
                        print('ok')
                    else:
                        print('No Such user Exists')

                print('Successfully created contact ')
                print('Success')
            except Exception as e:
                print(f'Failed to create contact: {e}')
                print('Failed ')
        except Exception as e:
            print(f'Failed to connect to db: {e}')'''

# l = log()
# l.login()
