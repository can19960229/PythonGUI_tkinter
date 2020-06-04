import tkinter, os	,tkinter.messagebox,tkinter.simpledialog,tkinter.ttk
from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
from tkinter.messagebox import showinfo, showwarning, showerror

from show_canvas_information import *
#先不导入 因为不会传参
# from show_conbobox import *

class show_canvas_nemu(object):
    def __init__(self,master = None):
        self.root = master  #定义内部变量root
      
        self.show_canvas_mynemu()
        #显示文本
        # self.show_text()
        self.getMyEntry()


    def show_canvas_mynemu(self):
        self.canvas_show_nemu = tkinter.Canvas(self.root, bg='red', height=120, width=1000)  # 创建绘图板 电感

        self.canvas_show_nemu.create_text(500, 50, text="请选择器件信息：", fill="yellow", font=("微软雅黑", 12))

        self.canvas_show_nemu.pack(side='top', fill='x')  # 画布显示

        # grid布局
        # self.canvas_show_inductor.grid(row=0, column=0)
        # self.canvas_show_resistor.grid(row=0, column=1)
        # self.canvas_show_capacitor.grid(row=0, column=2)

        #在menu中显示下拉框显示

        """
        # 不能直接调用类show_conbobox 因为无法获取参数  参数ERROR
        # 问题：需要获得这个canvas_menu的参数
        应该调用show_conbobox类中的方法 把固定的方法进行封装调用
        """

        self.combobox()


    def combobox(self):
        self.frame_show_combobox = tkinter.Frame(self.canvas_show_nemu,height=50, width=80,bg="yellow")  # 创建Frame
        tkinter.Label(self.frame_show_combobox, text="请选择器件：", font=("微软雅黑", 12),
                      justify="left").grid(row=0, column=0, sticky=tkinter.W)  # 显示标签
        equ_tuple = ("电阻", "电容", "电感")  # 下拉项
        self.equ_combobox = tkinter.ttk.Combobox(self.frame_show_combobox, height=5, width=15, values=equ_tuple)  # 列表项
        self.equ_combobox.bind("<<ComboboxSelected>>", self.show_data)  # 选项改变
        self.equ_combobox.grid(row=0, column=1)  # 显示组件


        self.frame_show_combobox.grid(row=0, column=0, sticky=tkinter.W)   # Frame显示
        self.content = tkinter.StringVar()  # 修改内容
        self.label = tkinter.Label(self.canvas_show_nemu, textvariable=self.content, font=("微软雅黑", 17), justify="right")  # 标签
        self.label.grid(row=2, column=0, sticky=tkinter.W)   # 显示标签

        self.frame_show_buttom = tkinter.Frame(self.canvas_show_nemu, height=50, width=80, bg="yellow")  # 创建Frame
        self.add_button()
        self.frame_show_buttom.grid(row=1, column=0,sticky=tkinter.W)
    def show_data(self, event):  # 事件处理
        get_ifo= self.equ_combobox.get()
        eqi_ifo = ["电感", "电容", "电阻"]  # 候选列表
        # 我就在information布局中加载button
        if(get_ifo == "电感"):

           """
           #下拉框选中了 在对应的canvas中显示器件  单数参数获取不了 
           self.show_button_inductor()  这是information栏中的函数
           """
           show_canvas_information.show_button_inductor()
            #未处理


        if (get_ifo == "电容"):

            """
             #下拉框选中了 在对应的canvas中显示器件  单数参数获取不了 
             self.show_button_capacitor()

             """
            # 未处理
        if (get_ifo == "电阻"):
            """
             #下拉框选中了 在对应的canvas中显示器件  单数参数获取不了 
             self.show_button_resistor()
             """
            # 未处理


        self.content.set("你选择的器件 ： %s" % self.equ_combobox.get())  # 内容显示
    def add_button(self):
        eqi_ifo = ["添加>>", "取消>>", "测试>>"]  # 候选列表
        for idx, val in enumerate(eqi_ifo):
            self.add_button = tkinter.Button(self.frame_show_buttom, text=val,
                                             fg="black", font=("微软雅黑", 11))  # 批量操作按钮
            self.add_button.pack(side="left",anchor='nw',padx=5, pady=5)  # 组件显示

    #在menu中添加文本信息 由于布局问题还没有很好的显示
    def show_text(self):

        # self.frame_show_myInputText = tkinter.Frame(self.canvas_show_nemu, height=50, width=150, bg="blue")
        # self.frame_show_myInputText.grid(row=0, column=2, rowspan=3, columnspan=3,sticky="E", padx=5, pady=5)

        self.frame_show_text = tkinter.Frame(self.canvas_show_nemu, height=50, width=150, bg="blue")  # 创建Frame
        # label_text = tkinter.Label(self.canvas_show_nemu,text="陈灿：",
        #                             bg="#223011",
        #                            font=("微软雅黑", 20), fg="#ffffff", justify="right")
        text = tkinter.Text(self.frame_show_text, width=50, height=5, font=("微软雅黑", 10))
        text.insert("current", "请输入...：")
        text.pack()
        self.frame_show_text.grid(row=0, column=2, rowspan=3, columnspan=3,
                                  sticky="E", padx=5, pady=5)

    #获得输入的文本信息事件
    def getMyEntry(self):
        self.my_entry = tkinter.Frame(self.canvas_show_nemu, bg="yellow", height=800, width=300)
        self.my_entry.grid(row=0, column=1, rowspan=3, columnspan=3,
                           sticky="E", padx=5, pady=5)  # Frame显示
        tkinter.Label(self.my_entry, text="请输入你要的器件信息：格式为1-X-Y-R/L/C-50", font=("微软雅黑", 12),
                      justify="left").pack(side='left', expand='no', anchor='nw', padx=5, pady=5)  # 显示标签
        self.input_mytext = tkinter.StringVar()
        self.inputEntry = tkinter.Entry(self.my_entry, borderwidth=5, width=40, textvariable=self.input_mytext)
        self.inputEntry.pack(side='left', expand='no', anchor='nw', padx=5, pady=5)
        self.ok_button = tkinter.Button(self.my_entry, height=1, width=5, text="OK",
                                              # image=self.image_inductor,
                                              compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.ok_button.pack(side='left', anchor='sw', padx=5, pady=5)  # 按钮显示
        self.inputEntry.bind('<Return>', self.OK)
    def OK(self,event):
        self.my_gettext = self.input_mytext.get()
        print(self.my_gettext)
        print(type(self.my_gettext))
        print(type(self.my_gettext.split("-")))
        print(self.my_gettext.split("-"))

        mylist = self.my_gettext.split("-")

        # 测试用户的输入并在后台进行显示
        for i, val in enumerate(mylist):
            print("序号：%s   值：%s" % (i + 1, val))



        self.equ = mylist[3]

        self.write = show_canvas_write()
        self.move_canvas = tkinter.Canvas(self.write, width=100, height=100, bg='white')

        #判断是电阻还是电容或者是电感
        if self.equ == 'C':
            self.components = CreatComponent.capacitor(self.move_canvas, x=20, y=20, xlen=100, ylen=20)
            self.move_canvas.pack(side='top', anchor='nw')
            # self.info_lable_No = tkinter.Label(self.move_canvas, text=self.component_info.No)
            # self.info_lable_No.place(x=0,y=0)
            self.move_canvas.bind("<B1-Motion>", self.MoveComponent)
            self.move_canvas.bind('<Button-3>', self.RightClickMenu)
            self.move_canvas.bind('<Double-Button-1>', self.doubleClick)

        elif self.equ == 'R':
            self.components = CreatComponent.resistor(self.move_canvas, x=20, y=20, xlen=100, ylen=20)
            self.move_canvas.pack(side='top', anchor='nw')
            self.move_canvas.bind("<B1-Motion>", self.MoveComponent)
            self.move_canvas.bind('<Button-3>', self.RightClickMenu)
            self.move_canvas.bind('<Double-Button-1>', self.doubleClick)

        elif self.equ == "L":
            self.components = CreatComponent.inductor(self.move_canvas, x=20, y=20, xlen=100, ylen=20)
            self.move_canvas.pack(side='top', anchor='nw')
            self.move_canvas.bind("<B1-Motion>", self.MoveComponent)
            self.move_canvas.bind('<Button-3>', self.RightClickMenu)
            self.move_canvas.bind('<Double-Button-1>', self.doubleClick)
        else:
            tkinter.messagebox.showinfo(title="提示",
                     message="轻按照格式输入要生成的期间！格式为：1-X-Y-R/L/C-50Ω")

        equ_ifo = mylist[4]
        if (mylist[3] == "L"):
            input_message = mylist[4] + "H"
        elif (mylist[3] == "C"):
            input_message = mylist[4] + "F"
        elif (mylist[3] == "R"):
            input_message = mylist[4] + "Ω"
        else:
            tkinter.messagebox.showinfo(title="提示",
                     message="轻按照格式输入要生成的期间！格式为：1-X-Y-R/L/C-50Ω")

        label_text = tkinter.Label(self.write, text=input_message, bg="#223011", font=("微软雅黑", 10),
                                   fg="#ffffff", justify="right")  # 创建标签
        # label_text.bind("<B1-Motion>", self.motion_handle)  # 鼠标左键拖动
        label_text.pack()  # 组件显示



    
