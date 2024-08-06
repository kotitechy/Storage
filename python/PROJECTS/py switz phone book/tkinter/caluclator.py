import tkinter as tk

root = tk.Tk()
# entry
e1 = tk.Entry(root)
# special
bac = tk.Button(root, text='ac')
beq = tk.Button(root, text='=')
# buttons
b0 = tk.Button(root, text='0')
b1 = tk.Button(root, text='1')
b2 = tk.Button(root, text='2')
b3 = tk.Button(root, text='3')
b4 = tk.Button(root, text='4')
b5 = tk.Button(root, text='5')
b6 = tk.Button(root, text='6')
b7 = tk.Button(root, text='7')
b8 = tk.Button(root, text='8')
b9 = tk.Button(root, text='9')
# operands
bp = tk.Button(root, text='+')
bm = tk.Button(root, text='-')
bpr = tk.Button(root, text='*')
bd = tk.Button(root, text='/')
# point
bdot = tk.Button(root, text='.')

# pack items
e1.place(x=10, y=10)
b1.place(x=10, y=10)
b2.place(x=10, y=10)
b3.place(x=10, y=10)
bp.place(x=10, y=10)
#
b4.place(x=10, y=10)
b5.place(x=10, y=10)
b6.place(x=10, y=10)
bm.place(x=10, y=10)
#
b7.place(x=10, y=10)
b8.place(x=10, y=10)
b9.place(x=10, y=10)
bpr.place(x=10, y=10)
#
b0.place(x=10, y=10)
bdot.place(x=10, y=10)
bac.place(x=10, y=10)
beq.place(x=10, y=10)

root.geometry("300x300")
root.mainloop()
