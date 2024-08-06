import tkinter as tk
from PIL import Image, ImageTk
from register import Crt_ac
from ch_bl import ch_bal
from transactions import trans
from user_dshb import UserDashboard

class SwiterzBankApp:
    def __init__(self, master):
        self.master = master
        self.master.title('SWITERZBANK')
        self.window_width = 700
        self.window_height = 500
        self.master.geometry(f"{self.window_width}x{self.window_height}")
        self.master.resizable(False, False)
        self.center_window()

        try:
            image1 = Image.open("wel.gif")
            self.gif1 = ImageTk.PhotoImage(image1)
            image2 = Image.open("wel.gif")
            self.gif2 = ImageTk.PhotoImage(image2)
        except FileNotFoundError as e:
            print(f"Error: {e}")

        self.label = tk.Label(self.master, image=self.gif1)
        self.label.pack()

        self.master.after(1000, self.update_label)
        self.master.after(3000, self.remove_label)
        self.after_welcome()

    def open_user_dashboard(self):
        user_dashboard_window = tk.Toplevel(self.master)
        user_dashboard = UserDashboard(user_dashboard_window)

    def check_balance(self):
        ch_bal_instance = ch_bal()
        ch_bal_instance.run()

    def open_transactions(self):
        transactions_instance = trans()
        transactions_instance.run()

    def after_welcome(self):
        header_l = tk.Label(self.master, text='SWITERZ BANK-MAIN', font=('Courier', 20, 'bold'))
        header_l.place(x=250, y=10)

        b1 = tk.Button(self.master, text='CREATE AC', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.create_account)
        b1.place(x=50, y=100)

        b2 = tk.Button(self.master, text='TRANSACTIONS', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.open_transactions)
        b2.place(x=50, y=170)

        b3 = tk.Button(self.master, text='USER DASH BOARD', font=('Arial', 12), bg='light blue', width=20, height=2,
                       command=self.open_user_dashboard)
        b3.place(x=250, y=100)

        b4 = tk.Button(self.master, text='CHECK BALANCE', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.check_balance)
        b4.place(x=250, y=170)

        b5 = tk.Button(self.master, text='HISTORY', font=('Arial', 12), bg='light blue', width=20, height=2)
        b5.place(x=450, y=100)

        b6 = tk.Button(self.master, text='GET DETAILS', font=('Arial', 12), bg='light blue', width=20, height=2)
        b6.place(x=450, y=170)

        b7 = tk.Button(self.master, text='ADMIN', font=('Arial', 12), bg='light blue', width=20, height=2)
        b7.place(x=50, y=400)

        b8 = tk.Button(self.master, text='EXIT', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.destroy)
        b8.place(x=250, y=400)

    def create_account(self):
        ac = Crt_ac()
        ac.run()

    def destroy(self):
        self.master.destroy()

    def update_label(self):
        if self.label["image"] == self.gif1:
            self.label["image"] = self.gif2
        else:
            self.label["image"] = self.gif1
        self.master.after(1000, self.update_label)

    def remove_label(self):
        self.label.destroy()
        self.after_welcome()

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.master.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

root = tk.Tk()
app = SwiterzBankApp(root)
root.mainloop()
