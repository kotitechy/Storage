import tkinter as tk
from tkinter import messagebox

import mysql.connector

class sin:
    def clk(self):
        n = self.usr.get().lower()
        p = self.passw.get().lower()
        print("Values :", n, " , ", p)

        try:
            db = mysql.connector.connect(host='192.168.23.173', user='root', passwd='root', database='phonebook')
            cur = db.cursor()
            print('Successfully connected to db')

            try:

                # Insert data into the user table
                cur.execute(f'INSERT INTO usr_table (name, contact) VALUES (%s, %s)', (n, p))
                db.commit()

                # Create the user table
                cur.execute(f'CREATE TABLE {n} (sno INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL, contact VARCHAR(15) NOT NULL)')
                db.commit()


                print(f'Successfully created {n} user with {p} password')
                messagebox.showerror("Success", f'Successfully created {n} user with {p} password')
            except Exception as e:

                # Update cache table (assuming cache is your main user table)
                # Assuming the 'cache' table has columns 'name' and 'pass'
                cur.execute(f'UPDATE cache SET name = %s WHERE sno = 1', (n,))
                db.commit()

                print(f'Successfully created {n} user with {p} password')
            except Exception as e:
                print(f'Failed to create user: {e}')
        except Exception as e:
            print(f'Failed to connect to database: {e}')

    def signin(self):
        sin = tk.Tk()
        sin.title('Signin')
        sin.geometry('300x300')
        self.usr = tk.Entry(sin)
        self.passw = tk.Entry(sin)
        self.usr.place(x=100, y=100)
        self.passw.place(x=100, y=150)
        usr_l = tk.Label(sin, text='Enter Email')
        passw_l = tk.Label(sin, text='Enter Passwd')
        usr_l.place(x=10, y=100)
        passw_l.place(x=10, y=150)
        con = tk.Button(sin, text='Create Ac', command=self.clk)
        con.place(x=100, y=200)
        sin.mainloop()


