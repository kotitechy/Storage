import tkinter as tk


class Creater_win:
    # questions and no of options per question
    no_of_q = 10
    no_of_op_p_q = 4

    # list for questions
    q_ls = []

    def cap_ques(self):
        x = self.no_of_q_e.get()
        print(f"{x} Questions Captured", x)

    def crt_ques(self):
        q = self.q_e.get()
        print(q)

    def crt_win(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Test Maker")

        self.no_of_q_l = tk.Label(self.root, text="No of Questions: ")
        self.no_of_q_l.place(x=50, y=30)

        self.no_of_q_e = tk.Entry(self.root, width=10)
        self.no_of_q_e.place(x=180, y=30)

        self.q_b = tk.Button(self.root, text='ok', command=self.cap_ques)
        self.q_b.place(x=250, y=30)

        self.q_l = tk.Label(self.root, text='Enter a Question Here: ')
        self.q_l.place(x=50, y=100)

        self.q_e = tk.Entry(self.root)
        self.q_e.place(x=180, y=100)

        x = 50
        y = 150
        nof_op = 4
        ls_label = []
        for i in range(0, nof_op + 1):
            self.O_l1 = tk.Label(self.root, text=f'Option-{i} ')
            self.O_l1.place(x=x, y=y)
            ls_label.append(self.O_l1)
            y += 50
        y = 150
        x = 180
        for i in range(0, nof_op + 1):
            self.o_e1 = tk.Entry(self.root)
            self.o_e1.place(x=x, y=y)
            y += 50

        self.sub = tk.Button(self.root, text='Next', command=self.cap_ques)
        self.sub.place(x=200, y=400)

        self.btn = tk.Button()
        self.root.mainloop()


c1 = Creater_win()
c1.crt_win()
