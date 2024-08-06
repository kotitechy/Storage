import tkinter as tk
import os, time

ls = []

def save(widget):
    r = widget.get("1.0", "end-1c")
    stats('saving file')
    f = open('file.txt', 'w')
    f.write(r)
    f.close()
    # stats('file saved')
    print('file saved')

def new_file():
    r = t1.get('1.0', 'end-1c')
    save()
    ls.append(r)
    print('prevoius file saved as: file.txt')

def stats(text):
    sts = tk.Label(root, text='')
    sts.place(x=10, y  = 411)
    # sts.config(text='')
    sts.config(text=text)


def menubar():
    #Menu
    menubar = tk.Menu(root) # top-level Menu
    root.config(menu=menubar)
    # file
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label='new', command=new_file)
    file_menu.add_command(label='open')
    file_menu.add_separator()
    file_menu.add_command(label='save', command=save)
    file_menu.add_command(label='save as')
    file_menu.add_separator()
    file_menu.add_command(label='print')
    file_menu.add_command(label='exit', command=root.destroy)
    menubar.add_cascade(label='file', menu=file_menu)
    # edit
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label='undo')
    file_menu.add_separator()
    file_menu.add_command(label='cut')
    file_menu.add_command(label='copy')
    file_menu.add_command(label='paste')
    file_menu.add_separator()
    file_menu.add_command(label='delete')
    file_menu.add_command(label='find')
    file_menu.add_command(label='replace')
    file_menu.add_command(label='select all')
    menubar.add_cascade(label='edit', menu=file_menu)
    #help
    file_menu = tk.Menubutton(menubar)
    menubar.add_cascade(label='help', menu=file_menu)

def newfile(t_name):
    t_name = tk.Text(root)
    t_name.place(x=20, y=20)

def widgets():
    t0 = tk.Button(root, width=5, background='red', command=save)
    t0.place(x=0, y=20)

    newfile('main.py')



root = tk.Tk()
root.title('NotePad Editor')
root.geometry('690x440')

widgets()

menubar()
stats('Welcome to text editor')


root.mainloop()

