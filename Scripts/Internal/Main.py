from Common import *
from Internal.add_data import *
from Internal.change_data import *
from Internal.statistics import *



class Main(tk.Frame):
    """
    Конструктор класса стартового окна
    Автор: Данилов Евгений Владимирович
    """
    
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        root_frame = tk.Frame()
        root_frame['bg'] = bgcolour1
        root_frame.pack(expand=1)
        btn_open_add_data = tk.Button(root_frame,
                                      text='Добавление данных', font="20",
                                      command=self.open_add_data, bg=btncolour,
                                      fg=btntextcolour,
                                      activebackground=btncolourpushed,
                                      compound=tk.TOP, width=20, height=3)
        btn_open_add_data.pack(expand=1, pady=20)
        btn_open_change_data = tk.Button(root_frame, text='Изменение данных',
                                         font="20",
                                         command=self.open_change_data,
                                         bg=btncolour, fg=btntextcolour,
                                         activebackground=btncolourpushed,
                                         compound=tk.TOP, width=20, height=3)
        btn_open_change_data.pack(expand=1, pady=20)
        btn_open_statistics = tk.Button(root_frame,
                                        text='Графики', font="20",
                                        command=self.open_statistics,
                                        bg=btncolour, fg=btntextcolour,
                                        activebackground=btncolourpushed,
                                        compound=tk.TOP, width=20, height=3)
        btn_open_statistics.pack(expand=1, pady=20)

    def open_add_data(self):
        add_data()

    def open_change_data(self):
        change_data()

    def open_statistics(self):
        statistics()

    