import tkinter as tk
from PIL import Image , Imagetk

def win(title,wid,heig,resize):
        win = tk.Tk()
        win.title(title)
        win.geometry(f'{wid}x{heig}')
        win.geometry(resize,resize)
        win.congig(bg='gray')

        win.mainloop()
