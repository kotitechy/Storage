import tkinter as tk
from PIL import Image, ImageTk
import register
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

        # Load GIFs with Pillow
        image1 = Image.open(r"C:\Users\SHIVA\Desktop\ATM\wel.gif")
        self.gif1 = ImageTk.PhotoImage(image1)

        image2 = Image.open(r"C:\Users\SHIVA\Desktop\ATM\wel.gif")
        self.gif2 = ImageTk.PhotoImage(image2)

        self.label = tk.Label(self.master, image=self.gif1)
        self.label.pack()

        # Schedule the update_label function to run periodically
        self.master.after(1000, self.update_label)

        # Schedule the removal of the label after 3 seconds
        self.master.after(3000, self.remove_label)

        self.after_welcome()

    def open_user_dashboard(self):
        user_dashboard_window = tk.Toplevel(self.master)
        user_dashboard = UserDashboard(user_dashboard_window)

    def chk_bal(self):
        ck = ch_bal()
        ck.run()

    def trans(self):
        # Create an instance of the ChBal class and run the application
        t = trans()
        t.run()
    def after_welcome(self):
        header_l = tk.Label(self.master, text='SWITERZ BANK-MAIN', font=('Courier', 20, 'bold'))
        header_l.place(x=250, y=10)

        # Button 1
        b1 = tk.Button(self.master, text='CREATE AC', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.create_ac)
        b1.place(x=50, y=100)

        # Button 2
        b2 = tk.Button(self.master, text='TRANSACTIONS', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.trans)
        b2.place(x=50, y=170)

        # Button 3
        b3 = tk.Button(self.master, text='USER DASH BOARD', font=('Arial', 12), bg='light blue', width=20, height=2,
                       command=self.open_user_dashboard)
        b3.place(x=250, y=100)

        # Button 4
        b4 = tk.Button(self.master, text='CHECK BALANCE', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.chk_bal)
        b4.place(x=250, y=170)

        # Button 5
        b5 = tk.Button(self.master, text='HISTORY', font=('Arial', 12), bg='light blue', width=20, height=2)
        b5.place(x=450, y=100)

        # Button 6
        b6 = tk.Button(self.master, text='GET DETAILS', font=('Arial', 12), bg='light blue', width=20, height=2)
        b6.place(x=450, y=170)

        # Button 7
        b7 = tk.Button(self.master, text='ADMIN', font=('Arial', 12), bg='light blue', width=20, height=2)
        b7.place(x=50, y=400)

        # Button 8
        b8 = tk.Button(self.master, text='EXIT', font=('Arial', 12), bg='light blue', width=20, height=2, command=self.des)
        b8.place(x=250, y=400)

    def create_ac(self):
        ac = register.Crt_ac()
        ac.run()

    def des(self):
        self.master.destroy()

    def update_label(self):
        # Switch between the two labels to create a simple animation
        if self.label["image"] == self.gif1:
            self.label["image"] = self.gif2
        else:
            self.label["image"] = self.gif1
        self.master.after(1000, self.update_label)

    def remove_label(self):
        self.label.destroy()  # Destroy the label widget to remove it
        self.after_welcome()

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.master.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SwiterzBankApp(root)
    root.mainloop()
