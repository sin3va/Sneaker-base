from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
from Common import *
from Internal.text import *

class change_data(tk.Toplevel):
    """
    Конструктор класса окна для просмотра и изменения данных
    Автор: Данилов Евгений Владимирович
    """

    def __init__(self):
        super().__init__()
        self.title('Изменение данных')
        self.geometry('650x500+435+100')
        self.resizable(False, False)
        self['bg'] = bgcolour1
        self.grab_set()
        self.focus_get()
        tk.Label(self, bg=bgcolour2).place(relx=0.05, rely=0.05,
                                           relwidth=0.9, relheight=0.83)
        self.lbl_2 = tk.Label(self, text='База данных №:', bg=bgcolour2)
        self.lbl_2.place(x=70, y=50)
        self.combo2 = Combobox(self, width=3, state='readonly')
        self.combo2.bind("<<ComboboxSelected>>", self.refresh)
        self.combo2.place(x=165, y=50)
        self.combo2['values'] = (1, 2)
        self.combo2.current(0)
        self.lbl_1 = tk.Label(self, text='Фильтр:', bg=bgcolour2)
        self.lbl_1.place(x=210, y=50)
        self.combo1 = Combobox(self, width=34, state='readonly')
        self.combo1.place(x=260, y=50)
        self.combo1['values'] = (
        'Без фильтра', 'Бренд', 'Модель', 'Год', 'Месяц', 'День', 'Идентификатор',
        'Розничная цена, $', 'Основной цвет')
        self.combo1.current(0)
        self.entry_lbl2 = tk.Entry(self, width=68, bg=bgcolour1)
        self.entry_lbl2.place(x=73, y=80)
        self.btn1 = tk.Button(self,
                              text='Вывести', command=self.output, bg=btncolour,
                              fg=btntextcolour,
                              activebackground=btncolourpushed, width=10)
        self.btn1.place(x=495, y=60)
        self.frame = tk.Frame(self, bg=bgcolour1)
        self.frame.place(relx=0.069, rely=0.22, relwidth=0.8615, relheight=0.57)

        self.btn_exitroot = tk.Button(self, text='Выход', bg=btncolour,
                                      fg=btntextcolour, width=8,
                                      activebackground=btncolourpushed,
                                      command=self.exitself)
        self.btn_exitroot.place(x=292, y=452)

    def refresh(self, event):
        """
        Функция для обновления списка фильтров в зависимосми от выбранной базы данных
        Принимает: ничего
        Возвращает: ничего
        Автор: Данилов Евгений Владимирович
        """
        if self.combo2.get() == '2':
            self.combo1['values'] = (
                'Без фильтра', 'Идентификатор', 'Средняя цена перепродажи в 2016, $',
                'Средняя цена перепродажи в 2017, $',
                'Средняя цена перепродажи в 2018, $',
                'Средняя цена перепродажи в 2019, $',
                'Средняя цена перепродажи в 2020, $')
            self.combo1.current(0)
        if self.combo2.get() == '1':
            self.combo1['values'] = (
            'Без фильтра', 'Бренд', 'Модель', 'Год', 'Месяц', 'День',
            'Идентификатор', 'Розничная цена, $', 'Основной цвет')
            self.combo1.current(0)

    def output(self):
        """
        Функция для вывода таблицы на экран
        Принимает: ничего
        Возвращает: ничего
        Автор: Данилов Евгений Владимирович
        """
        self.btn_save = tk.Button(self, text='Сохранить', bg=btncolour,
                                  fg=btntextcolour, width=8,
                                  activebackground=btncolourpushed,
                                  command=self.savec)
        self.btn_save.place(x=240, y=405)
        self.btn_del = tk.Button(self, text='Удалить', bg=btncolour,
                                 fg=btntextcolour, width=8,
                                 activebackground=btncolourpushed,
                                 command=self.delete)
        self.btn_del.place(x=340, y=405)
        for widget in self.frame.winfo_children():
            widget.destroy()
        if self.combo2.get() == '1':
            self.tree = Treeview(self.frame, column=(
                'Бренд', 'Модель', 'Год', 'Месяц', 'День', 'Идентификатор',
                'Розничная цена, $', 'Основной цвет'),
                                 height=13, show='headings')
            self.columns = ['Бренд', 'Модель', 'Год', 'Месяц', 'День',
                            'Идентификатор', 'Розничная цена, $', 'Основной цвет']
            self.tree.column('Бренд', width=70,
                             anchor=tk.CENTER)
            self.tree.column('Модель', width=310,
                             anchor=tk.CENTER)
            self.tree.column('Год', width=70,
                             anchor=tk.CENTER)
            self.tree.column('Месяц', width=70,
                             anchor=tk.CENTER)
            self.tree.column('День', width=70,
                             anchor=tk.CENTER)
            self.tree.column('Идентификатор', width=120,
                             anchor=tk.CENTER)
            self.tree.column('Розничная цена, $', width=110,
                             anchor=tk.CENTER)
            self.tree.column('Основной цвет', width=130,
                             anchor=tk.CENTER)
            self.tree.heading('Бренд', text='Бренд')
            self.tree.heading('Модель', text='Модель')
            self.tree.heading('Год', text='Год')
            self.tree.heading('Месяц', text='Месяц')
            self.tree.heading('День', text='День')
            self.tree.heading('Идентификатор', text='Идентификатор')
            self.tree.heading('Розничная цена, $', text='Розничная цена, $')
            self.tree.heading('Основной цвет', text='Основной цвет')

            self.bd_main = pd.read_pickle(bd1pth)
            ind = []
            for i in range(0, self.bd_main.shape[0]):
                ind.append(i)
            self.bd_main.index = list(ind)
            self.full_list = []
            for i in range(0, self.bd_main.shape[0]):
                self.list_row = []
                if self.combo1.get() == "Без фильтра":
                    if self.entry_lbl2.get() != '':
                        text('Сообщение',
                             'В режиме "Без фильтра" невозможен\nпоиск по ключевым словам')
                        self.entry_lbl2.delete(0, tk.END)
                    for j in self.bd_main.iloc[i]:
                        self.list_row.append(j)
                    self.full_list.append(self.list_row)
                if self.combo1.get() == "Бренд":
                    if str(self.bd_main.iloc[i][
                               'Brand']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Модель":
                    if str(self.bd_main.iloc[i][
                               'Model']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Год":
                    if str(self.bd_main.iloc[i][
                               'Year']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Месяц":
                    if str(self.bd_main.iloc[i][
                               'Month']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "День":
                    if str(self.bd_main.iloc[i][
                               'Day']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Идентификатор":
                    if str(self.bd_main.iloc[i][
                               'Id']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Розничная цена, $":
                    if str(self.bd_main.iloc[i][
                               'Retail']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Основной цвет":
                    if str(self.bd_main.iloc[i][
                               'Colour']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)

            if self.full_list == []:
                text('Сообщение',
                     'В таблице отсутствуют данные,\nудовлетворяющие запросу.')
            for row in self.full_list:
                self.tree.insert('', tk.END, values=row)

        if self.combo2.get() == '2':
            self.tree = Treeview(self.frame, column=(
                'Идентификатор', 'Средняя цена перепродажи в 2016, $',
                'Средняя цена перепродажи в 2017, $',
                'Средняя цена перепродажи в 2018, $',
                'Средняя цена перепродажи в 2019, $',
                'Средняя цена перепродажи в 2020, $'),
                                 height=13, show='headings')
            self.columns = ['Идентификатор', 'Средняя цена перепродажи в 2016, $',
                            'Средняя цена перепродажи в 2017, $',
                            'Средняя цена перепродажи в 2018, $',
                            'Средняя цена перепродажи в 2019, $',
                            'Средняя цена перепродажи в 2020, $']
            self.tree.column('Идентификатор', width=120,
                             anchor=tk.CENTER)
            self.tree.column('Средняя цена перепродажи в 2016, $', width=210,
                             anchor=tk.CENTER)
            self.tree.column('Средняя цена перепродажи в 2017, $', width=210,
                             anchor=tk.CENTER)
            self.tree.column('Средняя цена перепродажи в 2018, $', width=210,
                             anchor=tk.CENTER)
            self.tree.column('Средняя цена перепродажи в 2019, $', width=210,
                             anchor=tk.CENTER)
            self.tree.column('Средняя цена перепродажи в 2020, $', width=240,
                             anchor=tk.CENTER)
            self.tree.heading('Идентификатор', text='Идентификатор')
            self.tree.heading('Средняя цена перепродажи в 2016, $',
                              text='Средняя цена перепродажи в 2016, $')
            self.tree.heading('Средняя цена перепродажи в 2017, $',
                              text='Средняя цена перепродажи в 2017, $')
            self.tree.heading('Средняя цена перепродажи в 2018, $',
                              text='Средняя цена перепродажи в 2018, $')
            self.tree.heading('Средняя цена перепродажи в 2019, $',
                              text='Средняя цена перепродажи в 2019, $')
            self.tree.heading('Средняя цена перепродажи в 2020, $',
                              text='Средняя цена перепродажи в 2020, $')

            self.bd_main = pd.read_pickle(bd2pth)
            ind = []
            for i in range(0, self.bd_main.shape[0]):
                ind.append(i)
            self.bd_main.index = list(ind)
            self.full_list = []
            for i in range(0, self.bd_main.shape[0]):
                self.list_row = []
                if self.combo1.get() == "Без фильтра":
                    if self.entry_lbl2.get() != '':
                        text('Сообщение',
                             'В режиме "Без фильтра" невозможен\nпоиск по ключевым словам')
                        self.entry_lbl2.delete(0, tk.END)
                    for j in self.bd_main.iloc[i]:
                        self.list_row.append(j)
                    self.full_list.append(self.list_row)
                if self.combo1.get() == "Идентификатор":
                    if str(self.bd_main.iloc[i][
                               'Id']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Средняя цена перепродажи в 2016, $":
                    if str(self.bd_main.iloc[i][
                               'Medium resale price in 2016']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Средняя цена перепродажи в 2017, $":
                    if str(self.bd_main.iloc[i][
                               'Medium resale price in 2017']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Средняя цена перепродажи в 2018, $":
                    if str(self.bd_main.iloc[i][
                               'Medium resale price in 2018']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Средняя цена перепродажи в 2019, $":
                    if str(self.bd_main.iloc[i][
                               'Medium resale price in 2019']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)
                if self.combo1.get() == "Средняя цена перепродажи в 2020, $":
                    if str(self.bd_main.iloc[i][
                               'Medium resale price in 2020']).upper() == self.entry_lbl2.get().upper():
                        for j in self.bd_main.iloc[i]:
                            self.list_row.append(j)
                        self.full_list.append(self.list_row)

            if self.full_list == []:
                text('Сообщение',
                     'В таблице отсутствуют данные,\nудовлетворяющие запросу.')
            for row in self.full_list:
                self.tree.insert('', tk.END, values=row)

        self.scroll1 = tk.Scrollbar(self.frame, orient=tk.VERTICAL,
                                    command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scroll1.set)
        self.scroll1.pack(side=tk.RIGHT, fill=tk.Y)

        self.scroll2 = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL,
                                    command=self.tree.xview)
        self.tree.config(xscrollcommand=self.scroll2.set)
        self.scroll2.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.place(relwidth=1, relheight=1)

    def delete(self):
        """
        Функция для удаления строки из таблицы и обеих баз данных
        Принимает: ничего
        Возвращает: ничего
        втор: Данилов Евгений Владимирович
        """
        if self.tree.selection() == ():
            text('Ошибка', 'Выберите строчку для удаления.')
        else:
            self.treeid = self.tree.selection()[0]
            self.bd1 = pd.read_pickle(bd1pth)
            ind = []
            for i in range(0, self.bd1.shape[0]):
                ind.append(i)
            self.bd1.index = list(ind)
            self.bd2 = pd.read_pickle(bd2pth)
            ind = []
            for i in range(0, self.bd2.shape[0]):
                ind.append(i)
            self.bd2.index = list(ind)

            if 'Бренд' in self.columns:
                for i in range(len(self.bd1['Id'])):
                    if self.bd1['Id'][i] == \
                            self.tree.item(self.treeid, option='values')[5]:
                        self.bd1 = self.bd1.drop(i)
                self.bd1.to_pickle(bd1pth)

                for j in range(len(self.bd2['Id'])):
                    if self.bd2['Id'][j] == \
                            self.tree.item(self.treeid, option='values')[5]:
                        self.bd2 = self.bd2.drop(j)
                self.bd2.to_pickle(bd2pth)
                self.tree.delete(self.tree.selection()[0])
                self.tree.config(height=len(self.tree.get_children()))

            if 'Средняя цена перепродажи в 2016, $' in self.columns:
                for i in range(len(self.bd2['Id'])):
                    if self.bd2['Id'][i] == \
                            self.tree.item(self.treeid, option='values')[0]:
                        self.bd2 = self.bd2.drop(i)
                self.bd2.to_pickle(bd2pth)

                for j in range(len(self.bd1['Id'])):
                    if self.bd1['Id'][j] == \
                            self.tree.item(self.treeid, option='values')[0]:
                        self.bd1 = self.bd1.drop(j)
                self.bd1.to_pickle(bd1pth)
                self.tree.delete(self.tree.selection()[0])
                self.tree.config(height=len(self.tree.get_children()))

    def savec(self):
        """
        Функция для создания окна с предупреждением перед сохранением таблицы
        Принимает: ничего
        Возвращает: ничего
        Автор: Данилов Евгений Владимирович
        """
        self.mess = tk.Toplevel()
        self.mess.title('Сообщение')
        self.mess.geometry('300x130+635+300')
        self.mess.resizable(False, False)
        self.mess['bg'] = bgcolour1
        self.mess.grab_set()
        self.mess.focus_get()
        tk.Label(self.mess, bg=bgcolour1,
                 text='Для того, чтобы в сохраненной таблице\n'
                      'отсутствовали удаленные строки,\n'
                      'после их удаления необходимо\n'
                      'повторно нажать кнопку "Вывести".\n'
                      'Сохранить таблицу?').place(x=0, y=0, width=300,
                                                  height=80)
        btn_yes = tk.Button(self.mess, text='Да', bg=btncolour, fg=btntextcolour,
                            width=8,
                            activebackground=btncolourpushed, command=self.save)
        btn_yes.place(relx=0.23, rely=0.68)
        btn_no = tk.Button(self.mess, text='Нет', bg=btncolour, fg=btntextcolour,
                           width=8,
                           activebackground=btncolourpushed,
                           command=self.mess.destroy)
        btn_no.place(relx=0.56, rely=0.68)

    def save(self):
        """
        Функция для сохранения выведенной на экран таблицы
        Принимает: ничего
        Возвращает: ничего
        Автор: Данилов Евгений Владимирович
        """
        filename = 'База данных ' + self.combo2.get() + ' Фильтр ' + self.combo1.get() + '.csv'
        df_search = pd.DataFrame(self.full_list, columns=self.columns)

        file = tablepth + filename

        df_search.to_csv(file, index=None, header=True,
                         encoding="windows-1251", sep=';')
        text("Сообщение", "Таблица успешно сохранена в файл!")
        self.mess.destroy()

    def exitself(self):
        self.destroy()