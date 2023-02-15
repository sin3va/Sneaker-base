from Internal.Main import *

def MainF():
    app = Main(root)
    app.pack()
    root.title('SneakerAnalysis')
    root.geometry('650x500+435+100')
    root['bg'] = bgcolour1
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    MainF()
    
