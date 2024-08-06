import tkinter as tk
def clk():
    # Implement the logic for clk function
        # cur, db = con()
        un = usr.get()
        pas = passw.get()
        print("VALUES ARE : ",un,pas)

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
con = tk.Button(sin, text='Create Ac',command=clk)
con.place(x=100, y=200)
sin.mainloop()
# signin()

