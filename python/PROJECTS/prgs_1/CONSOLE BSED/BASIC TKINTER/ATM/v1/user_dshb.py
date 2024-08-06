import tkinter as tk

from ch_bl import ch_bal
from gen_atm_card import UpdateDetails
from gen_atm_pin import GenAPin


class UserDashboard:
    def chk_bal(self):
        ck = ch_bal()
        ck.run()

    def __init__(self, master):
        self.master = master
        self.master.title('SWITERZBANK')
        self.window_width = 700
        self.window_height = 500
        self.master.geometry(f"{self.window_width}x{self.window_height}")
        self.master.resizable(False, False)
        self.cen_window()

        self.header_label = tk.Label(self.master, text='SWITZ BANK \n\n USER DASHBOARD', font=('Courier', 20, 'bold'))
        self.header_label.place(x=250, y=10)

        self.b1 = tk.Button(self.master, text='GENERATE DEBIT CARD', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.gen_at)
        self.b1.place(x=50, y=130)

        self.b2 = tk.Button(self.master, text='GENERATE ATM PIN', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.gen_at_pin)
        self.b2.place(x=50, y=200)

        self.b3 = tk.Button(self.master, text='CHANGE/FORGOT PIN', font=('Arial', 12), bg='light blue', width=20, height=2)
        self.b3.place(x=250, y=130)

        self.b4 = tk.Button(self.master, text='CHECK BALANCE', font=('Arial', 12), bg='light blue', width=20, height=2,command=self.chk_bal)
        self.b4.place(x=250, y=200)

        self.b8 = tk.Button(self.master, text='EXIT', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.des)
        self.b8.place(x=250, y=400)

    def des(self):
        self.master.destroy()

    def gen_at(self):
        a = UpdateDetails()
    def gen_at_pin(self):
        gen_p = GenAPin()
        gen_p.run()

    def cen_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.master.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

