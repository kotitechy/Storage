import tkinter as tk
from PIL import ImageTk, Image
import sqlite3 as sl

class window:
    def con(self):
        try:
            db = sl.connect('msg.db')
            print('connected to db')
            try:
                cur = db.cursor()
                print('cursor created')
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        finally:
            return cur, db
    def get_det(self):
        email = self.e_i.get()
        passc = self.ps_i.get()
        print(email, passc)

    def validate_password(self):
        p=self.e7.get()
        p1=self.e8.get()
        f = 0
        if p == p1:
            self.st_l.config(text='password matched')
            f = 1
            return f
        else:
            self.st_l.config(text='invalid passwords')
            return f

    def ins_dat(self, name, email, phone, gender, dob, passwd):
        try:
            cur, db = self.con()
            q = "INSERT INTO user (name, email, phone, gender, dob, passwd) VALUES (?, ?, ?, ?, ?, ?)"
            # Ensure phone is a string before inserting into the database
            phone = str(phone)
            dat = (name, email, phone, gender, dob, passwd)
            cur.execute(q, dat)
            print('Data inserted successfully')
        except (sl.Error, sl.Error) as e:
            print('Error inserting data:', e)
        finally:
            try:
                db.commit()
            except (sl.Error, sl.Error) as e:
                print('Error committing changes:', e)
            finally:
                db.close()

    def get_dat(self):
        name = self.e1.get()
        email = self.e2.get()
        phone = self.e3.get()
        gender = self.e4.get()
        dob = self.e5.get()
        age = self.e6.get()
        pas1 = self.e7.get()
        pas2 = self.e8.get()
        self.ins_dat(name, email, phone, gender, dob, pas1)
        f = self.validate_password()
        if f==1:
            print('ok')
        else:
            print('not ok')


    def chk_usr_exits(self):
        pass

    def chk_error(self):
        pass

    def sign_in(self):
        self.e_l.destroy()
        self.ps_l.destroy()
        self.e_i.destroy()
        self.ps_i.destroy()
        self.sin_b.destroy()
        self.crt_ac.destroy()
        self.submit.destroy()

        self.logo.config(text='signin ')

        # labels
        self.l1 = tk.Label(self.root, text='name')
        self.l2 = tk.Label(self.root, text='email')
        self.l3 = tk.Label(self.root, text='phone')
        self.l4 = tk.Label(self.root, text='gender')
        self.l5 = tk.Label(self.root, text='dob')
        self.l6 = tk.Label(self.root, text='age')
        self.l7 = tk.Label(self.root, text='Enter password')
        self.l8 = tk.Label(self.root, text='Re-Enter password')

        # ok button
        self.btn = tk.Button(self.root, text='next')
        # entries
        self.e1 = tk.Entry(self.root)
        self.e2 = tk.Entry(self.root)
        self.e3 = tk.Entry(self.root)
        self.e4 = tk.Entry(self.root)
        self.e5 = tk.Entry(self.root)
        self.e6 = tk.Entry(self.root)
        self.e7 = tk.Entry(self.root)
        self.e8 = tk.Entry(self.root)
        # place labels
        self.l1.place(x=400, y=200)
        self.l2.place(x=400, y=250)
        self.l3.place(x=400, y=300)
        self.l4.place(x=400, y=350)
        self.l5.place(x=400, y=400)
        self.l6.place(x=400, y=450)
        self.l7.place(x=400, y=500)
        self.l8.place(x=400, y=550)
        # place entries
        self.e1.place(x=550, y=200)
        self.e2.place(x=550, y=250)
        self.e3.place(x=550, y=300)
        self.e4.place(x=550, y=350)
        self.e5.place(x=550, y=400)
        self.e6.place(x=550, y=450)
        self.e7.place(x=550, y=500)
        self.e8.place(x=550, y=550)
        # validate password button, stats-label
        self.v_pass = tk.Button(self.root, text='validate-pass', command=self.validate_password)
        self.v_pass.place(x=400, y=600)
        self.st_l = tk.Label(self.root, text='Enter pass')
        self.st_l.place(x=500, y=600)
        # submit
        self.sub = tk.Button(self.root, text='next', command=self.get_dat)
        self.sub.place(x=630, y=600)

    def des_signin(self):
        self.l1.destroy()
        self.l2.destroy()
        self.l3.destroy()
        self.l4.destroy()
        self.l5.destroy()
        self.l6.destroy()
        self.l7.destroy()
        self.l8.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.e3.destroy()
        self.e4.destroy()
        self.e5.destroy()
        self.e6.destroy()
        self.e7.destroy()
        self.e8.destroy()
        self.l1.destroy()
        self.l2.destroy()
        self.l3.destroy()
        self.l4.destroy()
        self.l5.destroy()
        self.l6.destroy()
        self.l7.destroy()
        self.l8.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.e3.destroy()
        self.e4.destroy()
        self.e5.destroy()
        self.e6.destroy()
        self.e7.destroy()
        self.e8.destroy()
        self.v_pass.destroy()
        self.st_l.destroy()
        self.sub.destroy()

    def g_s(self):
        self.l_l.destroy()
        self.g_s_b.destroy()
        self.pg1()

    def pg1(self):
        self.logo.config(text='login')

        # input
        # 1. email
        # 2. pass-code
        self.e_l = tk.Label(self.root, text='Enter Your Email-Id')
        self.ps_l = tk.Label(self.root, text='Enter Your Pass-code')
        self.e_l.place(x=500, y=200)
        self.ps_l.place(x=500, y=300)

        # input
        self.e_i = tk.Entry(self.root)
        self.ps_i = tk.Entry(self.root)
        self.e_i.place(x=500, y=250)
        self.ps_i.place(x=500, y=350)

        # submit
        self.submit = tk.Button(self.root, text='LogIn', command=self.get_det)
        self.submit.place(x=500, y=400)

        # signin
        self.crt_ac = tk.Label(self.root, text='Create an Account')
        self.crt_ac.place(x=500, y=500)
        self.sin_b = tk.Button(self.root, text='Signin', command=self.sign_in)
        self.sin_b.place(x=550, y=550)

    def win(self):
        self.root = tk.Tk()

        self.S_W = self.root.winfo_screenwidth()  # 1360
        self.S_H = self.root.winfo_screenheight()  # 768

        self.root.geometry(f'{self.S_W}x{self.S_H}')
        self.root.configure(bg='lavender')

        # image -- logo
        self.i_path = 'logo.png'
        self.image = Image.open(self.i_path)
        self.l_img = ImageTk.PhotoImage(self.image)
        self.l_l = tk.Label(self.root, image=self.l_img)
        self.l_l.place(x=100, y=100)

        self.logo = tk.Label(self.root, text='watsapp chat')
        self.logo.place(x=500, y=100)

        # get started button
        self.g_s_b = tk.Button(self.root, text='GET STARTED', command=self.g_s)
        self.g_s_b.place(x=500, y=300)

        self.root.mainloop()

    def on_enter(self, event):
        event.widget.config(bg="#CCCCCC")  # Change color to slightly gray when mouse enters

    def on_leave(self, event):
        event.widget.config(bg="#FFFFFF")  # Change color back to white when mouse leaves
    def cht_btn(self):

        self.button = tk.Button(self.can1, text="Hover Button", bg="#FFFFFF", bd=0, highlightthickness=0,
                           command=lambda: print("Button clicked"))
        self.i_x = 170
        self.i_y = 100
        self.button.place(x=self.i_x, y=self.i_y, anchor=tk.CENTER)

        # Bind events
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

        # Create rounded corners
        self.button.config(borderwidth=0)
        self.button.config(highlightthickness=0)
        self.button.config(relief=tk.FLAT)
        self.button.config(padx=150, pady=20)



    def chat(self):
        w = self.canvas.winfo_screenwidth() // 4
        h = self.canvas.winfo_screenheight()
        self.can1 = tk.Canvas(self.canvas, bg='white', width=w, height=h)
        self.can1.place(x=0, y=0)
        # chat label
        font = ("Helvetica", 20)
        self.c_s = tk.Label(self.can1, font=font, text='chats')
        self.c_s.place(x=10, y=10)
        # line
        self.can1.create_line(0, self.can1.winfo_screenheight() / 12, self.can1.winfo_screenwidth(),
                              self.can1.winfo_screenheight() / 12, fill="blue", width=5)





w = window()
w.win()
w.main_win()
