# main file
    def main_win(self):
        self.des_signin()
        self.logo.place(x=10, y=10)
        self.logo.config(text='watsapp')
        # logo , chat, group , news, profile
        self.s1 = tk.Button(self.root, text='chat', command=self.chat)
        self.s2 = tk.Button(self.root, text='news')
        self.s3 = tk.Button(self.root, text='groups')
        self.s4 = tk.Button(self.root, text='profile')
        # place buttons
        self.s1.place(x=100, y=10)
        self.s2.place(x=200, y=10)
        self.s3.place(x=300, y=10)
        self.s4.place(x=400, y=10)
        # canvas
        self.canvas = tk.Canvas(self.root, width=self.S_W - 200, height=self.S_H - 200, bg='red')
        self.canvas.place(x=50, y=50)

        self.cht_btn()
        w.main_win()