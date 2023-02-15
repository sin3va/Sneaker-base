from Common import *

class mistake(tk.Toplevel):
    """
    Конструктор класса окна с сообщением
    Автор: Данилов Евгений Владимирович
    """

    def __init__(self):
        super().__init__()
        self.title('Ошибка')
        self.geometry('300x100+635+300')
        self.resizable(False, False)
        self['bg'] = bgcolour1
        self.grab_set()
        self.focus_get()
        tk.Label(self, bg=bgcolour1,
                 text='Проверьте правильность и полноту\n'
                      'выбраннных/введенных данных\n'
                      'и попробуйте еще раз.').place(x=0, y=0, width=300,
                                                     height=50)
        btn_exitroot = tk.Button(self, text='Ок', bg=btncolour,
                                 fg=btntextcolour, width=8,
                                 activebackground=btncolourpushed,
                                 command=self.exitself)
        btn_exitroot.pack(side=tk.BOTTOM, pady=15)

    def exitself(self):
        self.destroy()