import tkinter, os	,tkinter.messagebox,tkinter.simpledialog,tkinter.ttk
from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
from tkinter.messagebox import showinfo, showwarning, showerror

#定义成了一个类 但是还没有实现调用 因为不知道怎么传参
class show_conbobox(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root

        #不能调用 因为获取参数错误
        self.combobox()
    #问题：需要获得这个canvas_menu的参数
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
        #下拉框的候选列表的事件处理
    def show_data(self, event):  # 事件处理
        get_ifo= self.equ_combobox.get()
        eqi_ifo = ["电感", "电容", "电阻"]  # 候选列表
        # 我就在information布局中加载button
        if(get_ifo == "电感"):
           self.show_button_inductor()
        if (get_ifo == "电容"):
            self.show_button_capacitor()
        if (get_ifo == "电阻"):
            self.show_button_resistor()

        self.content.set("你选择的器件 ： %s" % self.equ_combobox.get())  # 内容显示
    def add_button(self):
        eqi_ifo = ["添加>>", "取消>>", "测试>>"]  # 候选列表
        for idx, val in enumerate(eqi_ifo):
            self.add_button = tkinter.Button(self.frame_show_buttom, text=val,
                                             fg="black", font=("微软雅黑", 11))  # 批量操作按钮
            self.add_button.pack(side="left",anchor='nw',padx=5, pady=5)  # 组件显示

