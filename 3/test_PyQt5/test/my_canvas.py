import tkinter, os	,tkinter.messagebox,tkinter.simpledialog,tkinter.ttk
from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
from tkinter.messagebox import showinfo, showwarning, showerror
import time
from component_info import ComponentInfo
from component_creat import CreatComponent

LOGO_PATH = "D:\\chencan\\python\\PYECourse\\3\\venv\\resource\\logo.png"			# 图标
CAPACITOR_PATH = "D:\\chencan\\python\\PYECourse\\3\\venv\\resource\\2.png"
RESISTOR_PATH = "D:\\chencan\\python\\PYECourse\\3\\venv\\resource\\1.png"
INDUCTOR_PATH = "D:\\chencan\\python\\PYECourse\\3\\venv\\resource\\3.png"
class MainForm: 							# 主窗体
    def __init__(self): 						# 构造方法
        self.root = tkinter.Tk()  					# 创建窗体
        self.root.title("这是一个界面")  				# 设置窗体标题
        self.root.geometry("1000x1000")  					# 设置主窗体大小
        self.root.maxsize(1000, 1000)  					# 设置窗体最大尺寸
        self.root["background"] = "LightSlateGray"  				# 设置背景颜色
        self.root.protocol("WM_DELETE_WINDOW",self.close_handle)  # 设置protocol监听,进行关闭的提示
        # self.my_text()      #显示文本输入框
        self.create_menu()
        self.show_canvas()         #显示界面

        self.show_button_capacitor()  # 显示各个电阻电容的button
        self.show_button_inductor()
        self.show_button_resistor()

        # self.my_text()


        self.combobox()

        self.getMyEntry()

        self.root.mainloop()

    def rtnkey(event=None):
        print(e.get())
    def show_canvas(self):
        self.canvas_show_nemu = tkinter.Canvas(self.root,  height=50, width=500)  # 创建绘图板 电感
        self.canvas_show_information = tkinter.Canvas(self.root,height=100, width=250)       #信息显示栏
        #######################################################################

        self.canvas_write = tkinter.Canvas(self.root, height=800, width=600)  # 创建绘图板



        # 利用create_line()在画布上绘制直线

        CreatComponent.resistor(self.canvas_write, 200, 40, 100, 20)
        CreatComponent.resistor(self.canvas_write, 200, 100, 20, 100)
        CreatComponent.Dotframe(self.canvas_write,100,100,100,20)#横向一列1
        CreatComponent.Dotframe(self.canvas_write,350,100,100,20)#横向一列2

        CreatComponent.Dotframe(self.canvas_write,600,100,100,20)#纵向二列1
        # CreatComponent.Dotframe(self.canvas_write,350,100,20,100)#纵向二列2

        CreatComponent.Dotframe(self.canvas_write,100,100,20,100)#纵向一列1
        CreatComponent.Dotframe(self.canvas_write,100,350,20,100)#纵向一列2

        #######################################################################

        self.canvas_show_nemu.create_text(500, 50, text="请选择器件信息：", fill="yellow", font=("微软雅黑", 12))

        self.image_inductor = tkinter.PhotoImage(file=INDUCTOR_PATH)  # 底图对象
        self.canvas_show_nemu.create_image((0, 0), anchor=tkinter.NW)  # 图像
        self.image_resistor = tkinter.PhotoImage(file=RESISTOR_PATH)  # 底图对象
        self.image_capacitor = tkinter.PhotoImage(file=CAPACITOR_PATH)  # 底图对象

        self.canvas_show_nemu.pack(side='top', fill='x',padx=5, pady=5)  # 画布显示
        self.canvas_show_information.pack(side='left', expand='no', fill='y',padx=5, pady=5)  # 画布显示

        self.canvas_write.pack(side='right', expand='yes', padx=5, pady=5)  # 画布显示




    def show_button_inductor(self):
        # self.image_inductor = tkinter.PhotoImage(file=INDUCTOR_PATH)  # 底图对象
        self.button_inductor = tkinter.Button(self.canvas_show_information, height=80, width=150, text="电感", image=self.image_inductor,
                                              compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_inductor.pack(side='top', anchor='sw',padx=5, pady=5)  # 按钮显示
        self.button_inductor.bind("<Button-1>", lambda event: self.event_handle(event))  # 事件处理
    def show_button_resistor(self):
        self.button_resistor = tkinter.Button(self.canvas_show_information,height=80, width=150 , text="电阻", image=self.image_resistor,
                                         compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_resistor.pack(side='top', anchor='sw', fill='x',padx=5, pady=5)  # 按钮显示
    def show_button_capacitor(self):
        self.button_capacitor = tkinter.Button(self.canvas_show_information,height=80, width=150  , text="电容", image=self.image_capacitor,
                                          compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_capacitor.pack(side='top', anchor='sw',padx=5, pady=5)  # 按钮显示

    """
    范例函数：绑定电感的点击事件的函数
    """

    def event_button(self):
        self.button_inductor.bind("<Button-1>", lambda event: self.event_handle(event))  # 事件处理
    #下拉框
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
        tkinter.Label(self.canvas_show_nemu, textvariable=self.content, font=("微软雅黑", 17), justify="right").grid(row=2, column=0, sticky=tkinter.W)   # 显示标签

        self.frame_show_buttom = tkinter.Frame(self.canvas_show_nemu, height=50, width=80, bg="yellow")  # 创建Frame
        self.add_button()
        self.frame_show_buttom.grid(row=1, column=0,sticky=tkinter.W)
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
    # 单行文本框获取值
    def getMyEntry(self):
        self.my_entry = tkinter.Frame(self.canvas_show_nemu, bg="yellow", height=800, width=300)
        self.my_entry.grid(row=0, column=1,rowspan=3, columnspan=3,
           sticky="E", padx=5, pady=5)  # Frame显示
        tkinter.Label(self.my_entry, text="请输入你要的器件信息：格式为1-X-Y-R/L/C-50Ω", font=("微软雅黑", 12),
                      justify="left").pack(side='left', expand='no', anchor='nw', padx=5, pady=5)  # 显示标签
        self.input_mytext = tkinter.StringVar()
        self.inputEntry = tkinter.Entry(self.my_entry, borderwidth=5, width=50, textvariable=self.input_mytext)
        self.inputEntry.pack(side='top', expand='no', anchor='nw', padx=5, pady=5)
        self.inputEntry.bind('<Return>', self.OK)

    def OK(self, event):
        self.my_gettext = self.input_mytext.get()
        print(self.my_gettext)
        print(type(self.my_gettext))
        print(type(self.my_gettext.split("-")))
        print(self.my_gettext.split("-"))
        
        mylist = self.my_gettext.split("-")

        #测试用户的输入并在后台进行显示
        for i, val in enumerate(mylist):
            print("序号：%s   值：%s" % (i + 1, val))

        self.equ = mylist[3]

        self.move_canvas = tkinter.Canvas(self.canvas_write, width=100, height=100, bg='white')
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

        self.label_text = tkinter.Label(self.canvas_write, text=input_message, bg="#223011", font=("微软雅黑", 10),
                                   fg="#ffffff", justify="right")  # 创建标签
        # label_text.bind("<B1-Motion>", self.motion_handle)  # 鼠标左键拖动
        self.label_text.pack()  # 组件显示

    def MoveComponent(self,event):
        self.move_canvas.place(x=event.x_root, y=event.y_root) 			# 组件重新定位

    def RightClickMenu(self,event):
        self.menu = tkinter.Menu(self.canvas_write)
        self.menu.add_cascade(label='旋转')
        self.menu.post(event.x_root, event.y_root)

    def doubleClick(self,event):
        ComponentInfo.showComponent_info()
        # result = tkinter.messagebox.askokcancel(title='信息',message='111111')




    def creat_resistor(self):
        self.photo_R = tkinter.PhotoImage(file=RESISTOR_PATH)  # 电阻
        self.label_R = tkinter.Label(self.canvas_write, image=self.photo_R)  # 标签
        self.label_R.bind("<B1-Motion>", self.motion_handle)  # 鼠标左键拖动
        self.label_R.pack(side='left', expand='no', anchor='nw', padx=5, pady=5)  # 显示标签

    def creat_inductor(self):
        self.photo_I = tkinter.PhotoImage(file=INDUCTOR_PATH)  # 电感
        self.label_I = tkinter.Label(self.canvas_write, image=self.photo_I)  # 标签
        self.label_I.bind("<B1-Motion>", self.motion_handle)  # 鼠标左键拖动
        self.label_I.pack(side='left', expand='no', anchor='nw', padx=5, pady=5)  # 显示标签

    def creat_capcitor(self):
        self.photo_C = tkinter.PhotoImage(file=CAPACITOR_PATH)  # 电容
        self.label_C = tkinter.Label(self.canvas_write, image=self.photo_C)  # 标签
        self.label_C.bind("<B1-Motion>", self.motion_handle)  # 鼠标左键拖动
        self.label_C.pack(side='left', expand='no', anchor='nw', padx=5, pady=5)  # 显示标签

    def motion_handle(self, event):  # 事件处理函数
        self.label.place(x=event.x_root, y=event.y_root)  # 组件重新定位

    def event_handle(self, event):  # 事件处理函数
        input_message = tkinter.simpledialog.askstring("提示信息", "请输入要显示的信息：")

        label_text = tkinter.Label(self.canvas_write, text=input_message,bg="#223011", font=("微软雅黑", 10),
                                   fg="#ffffff", justify="right")  # 创建标签
        label_text.pack()  # 组件显示
    def create_menu(self):  # 创建菜单
        self.menu = tkinter.Menu(self.root)  # 创建菜单
        self.file_menu = tkinter.Menu(self.menu, tearoff=False)  # 创建子菜单
        self.file_menu.add_command(label="打开", command=self.menu_handle)  # 菜单项
        self.file_menu.add_command(label="保存", command=self.menu_handle)  # 菜单项
        self.file_menu.add_separator()  # 分割线
        self.file_menu.add_command(label="关闭", command=self.root.quit)  # 菜单项
        self.menu.add_cascade(label="文件", menu=self.file_menu)  # 追加子菜单
        self.edit_menu = tkinter.Menu(self.menu, tearoff=False)  # 创建子菜单
        self.edit_menu.add_command(label="剪切", command=self.menu_handle)  # 菜单项
        self.edit_menu.add_command(label="复制", command=self.menu_handle)  # 菜单项
        self.edit_menu.add_command(label="粘贴", command=self.menu_handle)  # 菜单项
        self.edit_menu.add_separator()  # 分割线
        self.edit_menu.add_command(label="设置", command=self.menu_handle)  # 菜单项
        self.menu.add_cascade(label="编辑", menu=self.edit_menu)  # 追加子菜单
        self.root.config(menu=self.menu)  # 菜单显示
        self.pop_menu = tkinter.Menu(self.root, tearoff=False)  # 弹出式菜单
        self.pop_menu.add_command(label="未处理的label", command=self.menu_handle)  # 菜单项
        self.pop_menu.add_command(label="未处理的label", command=self.menu_handle)  # 菜单项
        self.root.bind("<Button-3>", self.popup_handle)  # 绑定事件
    def menu_handle(self):  # 菜单处理
        pass  # 未定义处理函数体
    def popup_handle(self, event):  # 事件处理
        self.pop_menu.post(event.x_root, event.y_root)  # 菜单弹出


        #窗体关闭监听
    def close_handle(self):  # 事件处理函数
        if tkinter.messagebox.askyesnocancel("程序关闭确认", "这么好的程序真舍得关闭吗？？"):
            self.root.destroy()  # 关闭程序

def main():							# 主函数
    MainForm()							# 显示主窗体

if __name__ == "__main__":     					# 判断执行名称
    main()							# 调用主函数



