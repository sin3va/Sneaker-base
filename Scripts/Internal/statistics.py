from Common import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

class statistics(tk.Toplevel):
    """
    Конструктор класса окна для просмотра графиков
    Авторы: Данилов Евгений Владимирович, Гизатуллин Петр Олегович
    """

    def __init__(self):
        super().__init__()
        self.title('Статистика и графики')
        self.geometry('650x500+435+100')
        self.resizable(False, False)
        self.grab_set()
        self.focus_get()
        self['bg'] = bgcolour1
        tk.Label(self, bg=bgcolour2).place(relx=0.05, rely=0.05,
                                           relwidth=0.9, relheight=0.83)
        lbl_1 = tk.Label(self, text='Фильтр:', bg=bgcolour2)
        lbl_1.place(x=70, y=40)
        self.combo1 = Combobox(self, width=30, state='readonly')
        self.combo1.place(x=125, y=40)
        self.combo1['values'] = (
        'Бренд - Средняя цена', 'Модель - Средняя цена', 'Год - Средняя цена',)
        self.combo1.current(0)
        btn_graf = tk.Button(self, text='Построить график', bg=btncolour,
                             fg=btntextcolour,
                             activebackground=btncolourpushed,
                             command=self.graph_draw)
        btn_graf.place(x=340, y=40)
        btn_exitroot = tk.Button(self, text='Выход', bg=btncolour, fg=btntextcolour,
                                 width=8,
                                 activebackground=btncolourpushed,
                                 command=self.exitself)
        btn_exitroot.place(x=550, y=452)

    def graph_draw(self):
        """
        Функция для построения и вывода графиков
        Принимает: ничего
        Возвращает: ничего
        Автор: Гизатуллин Петр Олегович
        """
        self.help = tk.Frame(self, bg=bgcolour1)
        self.help.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=1)
        self.graph = tk.Frame(self.help, bg=bgcolour1)
        self.graph.place(relx=0, rely=-0.08, relwidth=1, relheight=0.9)
        if self.combo1.get() == 'Бренд - Средняя цена':
            fbd = pd.read_pickle(bd1pth)
            bd = brand_avgretail(fbd)
            fig = plt.figure(figsize=(4, 5), dpi=70)
            ax = fig.add_subplot(1, 1, 1)
            fig.suptitle('')
            bd.plot(kind='bar', ax=ax, x='Brand', y="Avg Retail", rot=45, fontsize=9)

        if self.combo1.get() == 'Модель - Средняя цена':
            fbd = pd.read_pickle(bd1pth)
            bd = model_avgretail(fbd)
            fig = plt.figure(figsize=(4, 5), dpi=70)
            ax = fig.add_subplot(1, 1, 1)
            fig.suptitle('')
            bd.plot(kind='bar', ax=ax, x='Model', y="Avg Retail", rot=45, fontsize=9)

        if self.combo1.get() == 'Год - Средняя цена':
            fbd = pd.read_pickle(bd1pth)
            bd = year_avgretail(fbd)
            fig = plt.figure(figsize=(4, 5), dpi=70)
            ax = fig.add_subplot(1, 1, 1)
            fig.suptitle('')
            bd.plot(kind='bar', ax=ax, x='Year', y="Avg Retail", rot=45, fontsize=9)

        CANVAS_1 = FigureCanvasTkAgg(fig, master=self.graph)
        CANVAS_1.draw()
        CANVAS_1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(CANVAS_1, self.graph)
        toolbar.update()
        CANVAS_1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        btn_exitroot = tk.Button(self, text='Выход', bg=btncolour, fg=btntextcolour,
                                 width=8,
                                 activebackground=btncolourpushed,
                                 command=self.exitself)
        btn_exitroot.place(x=550, y=452)

    def exitself(self):
        self.destroy()