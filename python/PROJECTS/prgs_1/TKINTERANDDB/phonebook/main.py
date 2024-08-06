import tkinter as tk
import mysql.connector

class main_win:
    usr_n = ''

    def cs(self):
        n = self.name.get().lower()
        mno = self.conct.get()
        print('Values : ', n, ' , ', mno)

        try:
            db = mysql.connector.connect(host='localhost', user='root', passwd='root')
            cur = db.cursor()
            print('Successfully connected to db')

            try:
                cur.execute('CREATE DATABASE IF NOT EXISTS phonebook')
                cur.execute('USE phonebook')

                # Assuming `cur` is your cursor object
                cur.execute(
                    f'CREATE TABLE IF NOT EXISTS {self.usr_n} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), contact VARCHAR(255))')
                db.commit()

                try:
                    cur.execute(f'INSERT INTO {self.usr_n} (name, contact) VALUES (%s, %s)', (n, mno))
                    db.commit()
                    self.stats1.config(text=f'Contact \n name : {n} \n Mobile no: {mno}')
                    print('Successfully created contact ')
                    # print('Success')
                except Exception as e:
                    print(e)

            except Exception as e:
                print(f'Failed to create contact: {e}')
                print('Failed ')

        except Exception as e:
            print(f'Failed to connect to db: {e}')


    def lis_c(self):
        # Create a Canvas widget
        canvas = tk.Canvas(self.phnbk, height=200, width=300)
        # canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        canvas.place(x=20,y=200)

        # Create a Scrollbar and associate it with the Canvas
        scrollbar = tk.Scrollbar(self.phnbk, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Canvas to use the Scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a Frame inside the Canvas to hold the content
        frame = tk.Frame(canvas)

        try:
            # Use a context manager to ensure proper handling of the connection
            with mysql.connector.connect(host='192.168.23.173', user='root', passwd='root', database='phonebook') as db:
                with db.cursor() as cur:
                    print('Successfully connected to db')
                    try:
                        cur.execute(f'SELECT * FROM {self.usr_n} ')
                        r = cur.fetchall()
                        s = cur.execute(f'SELECT COUNT(*) FROM {self.usr_n}')
                        s = cur.fetchone()
                        ps = f"Total {s} contacts"
                        print(ps)
                        if r:
                            for ri in r:
                                self.srh_stat.config(text=ps)
                                label = tk.Label(frame, text=f" {ri}")
                                label.pack()
                            print(r)
                        else:
                            label = tk.Label(frame, text=f"Zero contacts are found")
                            label.pack()
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
        # Bind the Frame to the Canvas
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)

        # Configure the Canvas to update the scroll region
        def on_frame_configure(event):
            # Update the scroll region to match the size of the Frame
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame.bind("<Configure>", on_frame_configure)

    def srch(self):
        try:
            # Use a context manager to ensure proper handling of the connection
            with mysql.connector.connect(host='localhost', user='root', passwd='root', database='phonebook') as db:
                with db.cursor() as cur:
                    print('Successfully connected to db')
                    try:
                        srh_c = self.srh.get()

                        # Use parameterized query to avoid SQL injection
                        cur.execute(f'SELECT * FROM {self.usr_n} WHERE name = %s', (srh_c,))

                        r = cur.fetchall()
                        if r:
                            self.srh_stat.config(text=r)
                            print(r)
                        else:
                            self.srh_stat.config(text='no such data found')
                            print('no such data found')
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)

    def mai(self, stater):
        self.phnbk = tk.Tk()
        self.phnbk.title(f'PhoneBook {self.usr_n}')
        self.phnbk.geometry('500x500')

        self.srh = tk.Entry(self.phnbk)
        self.srh.place(x=50, y=80)

        srhb = tk.Button(self.phnbk, text='SEARCH', command=self.srch)
        srhb.place(x=180, y=80)

        add_e = tk.Button(self.phnbk, text='Add new Contact', command=self.cs)
        add_e.place(x=350, y=80)

        self.name = tk.Entry(self.phnbk)
        self.name.place(x=350, y=120)

        self.conct = tk.Entry(self.phnbk)
        self.conct.place(x=350, y=160)

        nl = tk.Label(self.phnbk, text='NAME: ')
        conctl = tk.Label(self.phnbk, text='CONTACT: ')

        self.stats = tk.Label(self.phnbk, text=stater)
        self.stats.place(x=350, y=50)

        self.stats1 = tk.Label(self.phnbk, text='')
        self.stats1.place(x=350, y=200)

        self.srh_stat = tk.Label(self.phnbk,text='')
        self.srh_stat.place(x=10,y=100)

        nl.place(x=250, y=120)
        conctl.place(x=250, y=160)

        self.all_c = tk.Button(self.phnbk,text='List Contacts', command=self.lis_c)
        self.all_c.place(x=350,y=250)

        self.phnbk.stats_l = tk.Label(self.phnbk, text='Welcome')
        self.phnbk.stats_l.place(x=100, y=20)
        self.phnbk.mainloop()


    '''
    def add_c(n, c):
        # con(self)
        usr = "shiva"
        try:
            cur.execute(f'INSERT INTO {usr} VALUES (%s,%s)', (n, c))
            db.commit()
            print('Successfully created contact ')
            phnbk.stats_l.config(text='Success')
        except Exception as e:
            print(f'Failed to create contact: {e}')
            phnbk.stats_l.config(text='Failed ')
    def srch(self):
        # con()
        usr = 'shiva'
        try:
            r = cur.execute(f'SELECT * FROM {usr} WHERE name = %s', (usr,))
            if r:
                print('Contact found')
            else:
                print('No contact found')
        except Exception as e:
            print(f'Failed to load data/ \n No contact found: {e}')
        '''
# c = main_win()
# c.mai()
