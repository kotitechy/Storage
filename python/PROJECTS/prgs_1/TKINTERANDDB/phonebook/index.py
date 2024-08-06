import mysql.connector
import tkinter as tk

db = None
cur = None

def con():
    cur = None
    db = None
    try:
        db = mysql.connector.connect(host='localhost', user='root', passwd='root')
        cur = db.cursor()
        print('Successfully connected to db')
    except Exception as e:
        print(f'Failed to connect to db: {e}')
    
    return cur, db

def add_c(n, c):
    con()
    usr = "shiva"
    try:
        cur.execute(f'INSERT INTO {usr} VALUES (%s,%s)', (n, c))
        db.commit()
        print('Successfully created contact ')
        phnbk.stats_l.config(text='Success')
    except Exception as e:
        print(f'Failed to create contact: {e}')
        phnbk.stats_l.config(text='Failed ')

def srch():
    con()
    usr = 'shiva'
    try:
        r = cur.execute(f'SELECT * FROM {usr} WHERE name = %s', (usr,))
        if r:
            print('Contact found')
        else:
            print('No contact found')
    except Exception as e:
        print(f'Failed to load data/ \n No contact found: {e}')

def index():
    mai = tk.Tk()
    mai.title('Phone Book')
    mai.geometry('300x300')

    si_bn = tk.Button(mai, text='Sign in', command=signin)
    lg_bn = tk.Button(mai, text='Log in', command=login)

    si_bn.place(x=100, y=100)
    lg_bn.place(x=100, y=150)

    mai.mainloop()

def clk():
    # Implement the logic for clk function
        # cur, db = con()
        un = login.usr.get()
        pas = login.usr.get()
        print(un,pas)

def clks():
    # Implement the logic for clks function
    pass

def login():
    root = tk.Tk()
    root.title('Login')
    root.geometry('200x200')

    usr = tk.Entry(root)
    passw = tk.Entry(root)
    usr.place(x=100, y=100)
    passw.place(x=100, y=150)

    usr_l = tk.Label(root,text='Enter UserName')
    passw_l = tk.Label(root,text='Enter Passwd')
    usr_l.place(x=10, y=100)
    passw_l.place(x=10, y=150)
    
    con = tk.Button(root, text='Login', command=lambda un=username_entry.get(), p=password_entry.get(): login_logic(un, p))

    con.place(x=100, y=200)

    root.mainloop()

def signin():
    sin = tk.Tk()
    sin.title('Signin')
    sin.geometry('200x200')

    usr = tk.Entry(sin)
    passw = tk.Entry(sin)
    usr.place(x=100, y=100)
    passw.place(x=100, y=150)

    usr_l = tk.Label(sin,text='Enter UserName')
    passw_l = tk.Label(sin,text='Enter Passwd')
    usr_l.place(x=10, y=100)
    passw_l.place(x=10, y=150)

    con = tk.Button(sin, text='CReate Ac', command=clks)
    con.place(x=100, y=200)

    sin.mainloop()

def phnbk():
    global phnbk
    phnbk = tk.Tk()
    usr = 'shiva'
    phnbk.title(f'PhoneBook {usr}')
    phnbk.geometry('500x500')

    srh = tk.Entry(phnbk)
    srh.place(x=50, y=80)

    add_e = tk.Button(phnbk, text='Add new Contact', command=lambda: add_c(name.get(), conct.get()))
    add_e.place(x=300, y=80)

    name = tk.Entry(phnbk)
    name.place(x=300, y=120)

    conct = tk.Entry(phnbk)
    conct.place(x=300, y=160)

    phnbk.stats_l = tk.Label(phnbk, text='Welcome')
    phnbk.stats_l.place(x=100, y=20)

    phnbk.mainloop()

# You should call index() to start the application
index()
phnbk()