import tkinter as tk

import withdraw
from ch_bl import ch_bal
from deposit import Deposit  # Assuming Deposit is a class defined in deposit module

class trans:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('SWITZERBANK-USER-TRANSACTIONS')
        self.setup_window()

    def setup_window(self):
        window_width = 700
        window_height = 500
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)

        # Buttons
        self.create_button('DEPOSIT FUND', self.dep, 50, 100)
        self.create_button('WITHDRAW AMOUNT', self.withdraw, 50, 170)
        self.create_button('CHECK BALANCE', self.check_balance, 250, 100)

        # Label
        header_l = tk.Label(self.root, text='SWITZER BANK \n USER AUTHENTICATION', font=('Courier', 20, 'bold'))
        header_l.place(x=210, y=10)

    def create_button(self, text, command, x, y):
        button = tk.Button(self.root, text=text, font=('Arial', 12), bg='light blue', width=20, height=2, command=command)
        button.place(x=x, y=y)

    def dep(self):
        de = Deposit()
        de.run()

    def withdraw(self):
        wd = withdraw.withdraw()
        wd.run()

    def check_balance(self):
        c = ch_bal()
        c.run()

    def run(self):
        self.root.mainloop()

