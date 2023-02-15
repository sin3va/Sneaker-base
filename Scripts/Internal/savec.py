from Scripts.Common import *

class savec(tk.Toplevel):
    """
    Конструктор класса окна с сообщением
    Автор: Данилов Евгений Владимирович
    """

    def __init__(self):
        super().__init__()
        self.title('Сообщение')
        self.geometry('300x130+635+300')
        self.resizable(False, False)
        self['bg'] = bgcolour1
        self.grab_set()
        self.focus_get()
        tk.Label(self.mess, bg=bgcolour1,
                 text='Для того, чтобы в сохраненной таблице\n'
                      'отсутствовали удаленные строки,\n'
                      'после их удаления необходимо\n'
                      'повторно нажать кнопку "Вывести".\n'
                      'Сохранить таблицу?').place(x=0, y=0, width=300,
                                                  height=80)
        btn_yes = tk.Button(self, text='Да', bg=btncolour, fg=btntextcolour,
                            width=8, activebackground=btncolourpushed,
                            command=self.save)
        btn_yes.place(relx=0.23, rely=0.68)
        btn_no = tk.Button(self, text='Нет', bg=btncolour, fg=btntextcolour,
                           width=8, activebackground=btncolourpushed,
                           command=self.exitself)
        btn_no.place(relx=0.56, rely=0.68)

    def exitself(self):
        self.destroy()