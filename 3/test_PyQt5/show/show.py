from tkinter import *
from idlelib.tabbedpages import *


class MainFrame(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.master = master
        super(MainFrame, self).__init__(self.master, cnf)

        # create a menu 
        self.mmenu = Menu(root)
        self.master.config(menu=self.mmenu)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=W + E + N + S)

        self.BottomLabel = Label(self.master, text='top', width=1, bg='Blue')
        self.BottomLabel.pack(side=TOP, expand=NO, fill=X)

        self.BottomLabel = Label(self.master, text='bottom', width=1, bg='Blue')
        self.BottomLabel.pack(side=BOTTOM, expand=NO, fill=X)

        self.LeftCanv = Canvas(self.master, bg='Blue', width=175, height=30)
        self.LeftCanv.pack(side=LEFT, expand=NO, fill=Y)  # padx=10, pady=5, ipadx=5, ipady=5,
        # self.LeftCanv.grid( row = 0, column = 0, sticky = W+E+N+S )
        # self.tabPage=TabbedPageSet(self.master, page_names=['Foobar','Baz'], n_rows=0,
        #                  expand_tabs=False#,width = 175, height = 30  
        #                  ) 
        # self.tabPage.pack(side=LEFT, expand=NO, fill=BOTH)

        self.MidLabel = Label(self.master, text='', width=0, cursor='sb_h_double_arrow')
        self.MidLabel.pack(side=LEFT, expand=NO, fill=Y)
        self.MidLabel.bind("<B1-Motion>", self.SetLeftCanvSize)

        self.RightCanv = Canvas(self.master, bg='Pink')
        self.RightCanv.pack(side=RIGHT, expand=YES, fill=BOTH)
        obj1 = self.RightCanv.create_text(50, 30, text='Click me one')
        # self.RightCanv.grid( row=0, column=1, sticky = W+E+N+S )

        self.AddMenu()

    def AddMenu(self):
        filemenu = Menu(self.mmenu)
        filemenu.add_command(label="New", command=self.quit)
        filemenu.add_command(label="Open...", command=self.quit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        self.mmenu.add_cascade(label="File", menu=filemenu)

        configmenu = Menu(self.mmenu)
        configmenu.add_command(label="我的设置", command=self.quit)
        self.mmenu.add_cascade(label="设置", menu=configmenu)

    def SetLeftCanvSize(self, event):
        self.LeftCanv.config(width=self.LeftCanv.winfo_width() + event.x - 7)
        # self.tabPage.config(width=self.tabPage.winfo_width()+event.x-7)

    def __del__(self):
        print('退出')


if __name__ == '__main__':
    root = Tk()
    MF = MainFrame(root, width=800, height=600)
    MF.pack()
    root.mainloop() 