from Common import *
from tkinter.ttk import Combobox
from Internal.text import *
from Internal.mistake import *
from Internal.ready import *

class add_data(tk.Toplevel):
    """
    Конструктор класса окна для добавления данных
    Автор: Данилов Евгений Владимирович
    """

    def __init__(self):
        super().__init__()
        self.title('Добавление данных')
        self.geometry('650x500+435+100')
        self.resizable(False, False)
        self.grab_set()
        self.focus_get()
        self['bg'] = bgcolour1
        tk.Label(self, bg=bgcolour2).place(relx=0.05, rely=0.05,
                                           relwidth=0.9, relheight=0.83)
        tk.Label(self, text='Введите данные:', font=20,
                 bg=bgcolour2).place(relx=0.05, rely=0.1, relwidth=0.9)

        self.lbl_1 = tk.Label(self, text='Бренд:', bg=bgcolour2)
        self.lbl_1.place(x=70, y=100)
        self.entry_lbl1 = tk.Entry(self, width=20)
        self.entry_lbl1.place(x=115, y=100)
        self.lbl_2 = tk.Label(self, text='Модель:', bg=bgcolour2)
        self.lbl_2.place(x=265, y=100)
        self.entry_lbl2 = tk.Entry(self, width=40)
        self.entry_lbl2.place(x=320, y=100)
        self.lbl_3 = tk.Label(self, text='Год:', bg=bgcolour2)
        self.lbl_3.place(x=70, y=130)
        self.entry_lbl3 = tk.Entry(self, width=7)
        self.entry_lbl3.place(x=100, y=130)
        self.lbl_4 = tk.Label(self, text='Месяц:', bg=bgcolour2)
        self.lbl_4.place(x=150, y=130)
        self.combo1 = Combobox(self, width=10, state='readonly')
        self.combo1.place(x=200, y=130)
        self.combo1['values'] = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май',
                                 'Июнь', 'Июль', 'Август', 'Сентябрь',
                                 'Октябрь', 'Ноябрь', 'Декабрь')
        self.combo1.current(0)
        self.lbl_5 = tk.Label(self, text='День:', bg=bgcolour2)
        self.lbl_5.place(x=290, y=130)
        self.combo2 = Combobox(self, width=3, state='readonly')
        self.combo2.place(x=330, y=130)
        self.combo2['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                 26, 27, 28, 29, 30, 31)
        self.combo2.current(0)
        self.lbl_7 = tk.Label(self, text='Идентификатор:', bg=bgcolour2)
        self.lbl_7.place(x=380, y=130)
        self.entry_lbl7 = tk.Entry(self, width=14)
        self.entry_lbl7.place(x=477, y=130)
        self.lbl_8 = tk.Label(self, text='Розничная цена, $:', bg=bgcolour2)
        self.lbl_8.place(x=70, y=160)
        self.entry_lbl8 = tk.Entry(self, width=5)
        self.entry_lbl8.place(x=180, y=160)
        self.lbl_9 = tk.Label(self, text='Основной цвет:', bg=bgcolour2)
        self.lbl_9.place(x=220, y=160)
        self.entry_lbl9 = tk.Entry(self, width=15)
        self.entry_lbl9.place(x=315, y=160)
        self.lbl_10 = tk.Label(self,
                               text='Средняя цена перепродажи в 2016 году, $:',
                               bg=bgcolour2)
        self.lbl_10.place(x=70, y=190)
        self.entry_lbl10 = tk.Entry(self, width=5)
        self.entry_lbl10.place(x=310, y=190)
        self.lbl_11 = tk.Label(self,
                               text='Средняя цена перепродажи в 2017 году, $:',
                               bg=bgcolour2)
        self.lbl_11.place(x=70, y=220)
        self.entry_lbl11 = tk.Entry(self, width=5)
        self.entry_lbl11.place(x=310, y=220)
        self.lbl_12 = tk.Label(self,
                               text='Средняя цена перепродажи в 2018 году, $:',
                               bg=bgcolour2)
        self.lbl_12.place(x=70, y=250)
        self.entry_lbl12 = tk.Entry(self, width=5)
        self.entry_lbl12.place(x=310, y=250)
        self.lbl_13 = tk.Label(self,
                               text='Средняя цена перепродажи в 2019 году, $:',
                               bg=bgcolour2)
        self.lbl_13.place(x=70, y=280)
        self.entry_lbl13 = tk.Entry(self, width=5)
        self.entry_lbl13.place(x=310, y=280)
        self.lbl_14 = tk.Label(self,
                               text='Средняя цена перепродажи в 2020 году, $:',
                               bg=bgcolour2)
        self.lbl_14.place(x=70, y=310)
        self.entry_lbl14 = tk.Entry(self, width=5)
        self.entry_lbl14.place(x=310, y=310)
        self.btn2 = tk.Button(self,
                              text='Добавить', command=self.add2, bg=btncolour,
                              fg=btntextcolour,
                              activebackground=btncolourpushed,
                              compound=tk.TOP, width=10, height=2)
        self.btn2.place(x=284, y=360)
        self.btn_exitroot = tk.Button(self, text='Выход', bg=btncolour,
                                      fg=btntextcolour, width=8,
                                      activebackground=btncolourpushed,
                                      command=self.exitself)
        self.btn_exitroot.place(x=292, y=452)

    def add2(self):
        """
        Функция для добавления введенных данных в базы данных
        Принимает: ничего
        Возвращает: ничего
        Автор: Данилов Евгений Владимирович
        """
        f = 0
        self.bd1 = pd.read_pickle(bd1pth)
        ind = []
        for i in range(0, self.bd1.shape[0]):
            ind.append(i)
        self.bd1.index = list(ind)
        for i in range(len(self.bd1['Id'])):
            if self.bd1['Id'][i] == self.entry_lbl7.get():
                f += 1
        if f > 0:
            text('Ошибка', 'Позиция с таким идентификатором уже есть в базе.')
        elif self.entry_lbl1.get() == '' or self.entry_lbl2.get() == '' or \
                self.entry_lbl3.get() == '' or self.combo1.get() == '' or self.combo2.get() == '' or \
                self.entry_lbl7.get() == '' or self.entry_lbl8.get() == '' or self.entry_lbl9.get() == '':
            mistake()

        elif (
                self.entry_lbl10.get() == '' and self.entry_lbl11.get() == '' and self.entry_lbl12.get() == '' and self.entry_lbl13.get() == '' and self.entry_lbl14.get() == ''):
            mistake()
        elif (self.entry_lbl10.get() != '' and not (
        self.entry_lbl10.get()).isdigit()) or (self.entry_lbl11.get() != '' and
                                               not (
                                               self.entry_lbl11.get()).isdigit()) or (
                self.entry_lbl12.get() != '' and not (
        self.entry_lbl12.get()).isdigit()) \
                or (self.entry_lbl13.get() != '' and not (
        self.entry_lbl13.get()).isdigit()) or (self.entry_lbl14.get() != '' and not
        (self.entry_lbl14.get()).isdigit()) or (self.entry_lbl3.get() != '' and not (
        self.entry_lbl3.get()).isdigit()) or (self.entry_lbl8.get() != '' and not (
        self.entry_lbl8.get()).isdigit()):
            mistake()
        elif int(self.entry_lbl3.get()) == 2017 and (
                self.entry_lbl11.get() == '' or self.entry_lbl12.get() == '' or self.entry_lbl13.get() == '' or self.entry_lbl14.get() == ''):
            mistake()
        elif int(self.entry_lbl3.get()) == 2018 and (
                self.entry_lbl12.get() == '' or self.entry_lbl13.get() == '' or self.entry_lbl14.get() == ''):
            mistake()
        elif int(self.entry_lbl3.get()) == 2019 and (
                self.entry_lbl13.get() == '' or self.entry_lbl14.get() == ''):
            mistake()
        elif int(self.entry_lbl3.get()) == 2020 and (self.entry_lbl14.get() == ''):
            mistake()
        elif self.entry_lbl1.get() == '' or self.entry_lbl2.get() == '' or self.entry_lbl3.get() == '' or self.combo1.get() == '' or self.combo2.get() == '' or self.entry_lbl7.get() == '' or self.entry_lbl8.get() == '' or self.entry_lbl9.get() == '':
            mistake()

        else:
            pd.read_pickle(bd1pth).append(
                {'Brand': self.entry_lbl1.get(), 'Model': self.entry_lbl2.get(),
                 'Year': self.entry_lbl3.get(),
                 'Month': self.combo1.get(), 'Day': self.combo2.get(),
                 'Id': self.entry_lbl7.get(),
                 'Retail': self.entry_lbl8.get(), 'Colour': self.entry_lbl9.get()},
                ignore_index=True).to_pickle(
                bd1pth)
            pd.read_pickle(bd2pth).append({'Id': self.entry_lbl7.get(),
                                           'Medium resale price in 2016': self.entry_lbl10.get(),
                                           'Medium resale price in 2017': self.entry_lbl11.get(),
                                           'Medium resale price in 2018': self.entry_lbl12.get(),
                                           'Medium resale price in 2019': self.entry_lbl13.get(),
                                           'Medium resale price in 2020': self.entry_lbl14.get()},
                                          ignore_index=True).to_pickle(bd2pth)
            ready()
            self.entry_lbl1.delete(0, tk.END)
            self.entry_lbl2.delete(0, tk.END)
            self.entry_lbl3.delete(0, tk.END)
            self.combo1.current(0)
            self.combo2.current(0)
            self.entry_lbl7.delete(0, tk.END)
            self.entry_lbl8.delete(0, tk.END)
            self.entry_lbl9.delete(0, tk.END)
            self.entry_lbl10.delete(0, tk.END)
            self.entry_lbl11.delete(0, tk.END)
            self.entry_lbl12.delete(0, tk.END)
            self.entry_lbl13.delete(0, tk.END)
            self.entry_lbl14.delete(0, tk.END)

    def exitself(self):
        self.destroy()