import tkinter as tk
import pandas as pd

root = tk.Tk()
backgroundcolour1 = tk.StringVar()
backgroundcolour1.set('')
backgroundcolour2 = tk.StringVar()
backgroundcolour2.set('')
buttoncolour = tk.StringVar()
buttoncolour.set('')
buttontextcolour = tk.StringVar()
buttontextcolour.set('')
buttoncolourpushed = tk.StringVar()
buttoncolourpushed.set('')
bd1path = tk.StringVar()
bd1path.set('')
bd2path = tk.StringVar()
bd2path.set('')
graphpath = tk.StringVar()
graphpath.set('')
tablepath = tk.StringVar()
tablepath.set('')
config = open('Scripts\configuration.txt')

for line in config:
    line = line[:-1]
    if line[0] == '-':
        pass
    elif backgroundcolour1.get() == '':
        backgroundcolour1.set(line)
    elif backgroundcolour2.get() == '':
        backgroundcolour2.set(line)
    elif buttoncolour.get() == '':
        buttoncolour.set(line)
    elif buttontextcolour.get() == '':
        buttontextcolour.set(line)
    elif buttoncolourpushed.get() == '':
        buttoncolourpushed.set(line)
    elif bd1path.get() == '':
        bd1path.set(line)
    elif bd2path.get() == '':
        bd2path.set(line)
    elif graphpath.get() == '':
        graphpath.set(line)
    elif tablepath.get() == '':
        tablepath.set(line)
bgcolour1 = backgroundcolour1.get()
bgcolour2 = backgroundcolour2.get()
btncolour = buttoncolour.get()
btntextcolour = buttontextcolour.get()
btncolourpushed = buttoncolourpushed.get()
bd1pth = bd1path.get()
bd2pth = bd2path.get()
tablepth = tablepath.get()
graphpth = graphpath.get()


def brand_avgretail(firstbd):
    """
    Функция, создающая DataFrame по фильтрам
    Принимает: firstbd
    Возвращает: avgretbr
    Автор: Гизатуллин Петр Олегович
    """
    general = pd.DataFrame(firstbd)
    general['Retail'] = general['Retail'].apply(pd.to_numeric, errors='coerce')
    avgretbr = general.groupby(['Brand']).agg({'Retail': "mean"})
    avgretbr.rename(columns={'Brand': 'Brand', 'Retail': 'Avg Retail'},
                    inplace=True)
    avgretbr = avgretbr.reset_index()
    return avgretbr


def model_avgretail(firstbd):
    """
    Функция, создающая DataFrame по фильтрам
    Принимает: firstbd
    Возвращает: avgretmod
    Автор: Гизатуллин Петр Олегович
    """
    general = pd.DataFrame(firstbd)
    general['Retail'] = general['Retail'].apply(pd.to_numeric, errors='coerce')
    avgretmod = general.groupby(['Model']).agg({'Retail': "mean"})
    avgretmod.rename(columns={'Model': 'Model', 'Retail': 'Avg Retail'},
                     inplace=True)
    avgretmod = avgretmod.reset_index()
    return avgretmod


def year_avgretail(firstbd):
    """
    Функция, создающая DataFrame по фильтрам
    Принимает: firstbd
    Возвращает: avgretmod
    Автор: Гизатуллин Петр Олегович
    """
    general = pd.DataFrame(firstbd)
    general['Retail'] = general['Retail'].apply(pd.to_numeric, errors='coerce')
    avgretyear = general.groupby(['Year']).agg({'Retail': "mean"})
    avgretyear.rename(columns={'Year': 'Year', 'Retail': 'Avg Retail'},
                      inplace=True)
    avgretyear = avgretyear.reset_index()
    return avgretyear

def open_config():
    """
    Функция для чтения конфигурационного файла
    Принимает: ничего
    Возвращает: ничего
    Автор: Данилов Евгений Владимирович
    """
    