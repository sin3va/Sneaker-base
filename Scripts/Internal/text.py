from Common import *

class text(tk.Toplevel):
    """
    Конструктор класса окна с сообщением
    Автор: Данилов Евгений Владимирович
    """

    def __init__(self, str1, str2):
        super().__init__()
        self.title(str1)
        self.geometry('300x100+635+300')
        self.resizable(False, False)
        self['bg'] = bgcolour1
        self.grab_set()
        self.focus_get()
        tk.Label(self, bg=bgcolour1,
                 text=str2).place(x=0, y=0, width=300, height=50)
        btn_exitroot = tk.Button(self, text='Ок', bg=btncolour,
                                 fg=btntextcolour, width=8,
                                 activebackground=btncolourpushed,
                                 command=self.exitself)
        btn_exitroot.pack(side=tk.BOTTOM, pady=15)

    def exitself(self):
        self.destroy()