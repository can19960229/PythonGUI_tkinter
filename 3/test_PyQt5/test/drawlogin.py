import tkinter, os	,tkinter.messagebox,tkinter.simpledialog,tkinter.ttk

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
        self.show_equipment()         #显示界面
        self.src_listbox()              # 显示器件信息列表
        self.button()       #显示各个电阻电容的button
        self.oper_button()  # 显示操作按钮
        self.dest_listbox()  # 显示器件已添加的
        # self.my_text()
        self.combobox()
        self.root.mainloop()




    def frame_show(self):
        message_show_Frame = tkinter.Frame(height=200, width=300)  # 创建<消息列表分区 >
        message_send_Frame = tkinter.Frame(height=200, width=300)  # 创建<发送消息分区 >
        button_Frame = tkinter.Frame(height=200, width=300)  # 创建<按钮分区>
        pic_right_Frame = tkinter.Frame(height=600, width=100)  # 创建<图片分区>

        ##  Frame在主控件上的布局
        message_show_Frame.grid(row=0, column=0)
        message_send_Frame.grid(row=1, column=0)
        button_Frame.grid(row=2, column=0)
        pic_right_Frame.grid(row=0, column=1, rowspan=3)


        ## 输出Text
        txt_msglist = tkinter.Text(message_show_Frame)
        txt_msglist.tag_config('green', foreground='blue')  # 创建标签，不懂
        txt_msglist.grid()

        # ## 输入框Text
        # txt_msgsend = tkinter.Text(message_send_Frame)
        # txt_msgsend.bind('<KeyPress-Up>', msgsendEvent)  # 绑定‘UP’键与消息发送。
        # txt_msgsend.grid()

        # ## 发送按钮
        # button_send = tkinter.Button(button_Frame, text='Send', command=msgsend)
        # button_send.grid(row=0, column=0, sticky=W)  # 在Frame f_floor上的布局设置
        #
        # ## 取消按钮
        # button_cancel = tkinter.Button(button_Frame, text='Cancel', command=cancel)
        # button_cancel.grid(row=0, column=1, sticky=W)

        ## 标签显示图片
        photo = tkinter.PhotoImage(file=LOGO_PATH)
        label = tkinter.Label(pic_right_Frame, image=photo)
        label.image = photo
        label.grid()

    def show_equipment(self):
        self.canvas_show_inductor = tkinter.Canvas(self.root,bg='red',height=50, width=500)  # 创建绘图板 电感
        self.canvas_show_resistor = tkinter.Canvas(self.root,bg='yellow',  height=50, width=120)  # 创建绘图板   电阻
        self.canvas_show_capacitor = tkinter.Canvas(self.root,bg='blue', height=50, width=120)  # 创建绘图板   电容
        self.canvas_show_information = tkinter.Canvas(self.root,bg='yellow',height=100, width=250)       #信息显示栏
        self.canvas_write = tkinter.Canvas(self.root,bg='green', height=900, width=200)  # 创建绘图板

        # self.canvas_show_inductor = tkinter.Canvas(self.root ,height=50, width=500)  # 创建绘图板 电感
        # self.canvas_show_resistor = tkinter.Canvas(self.root,  height=50, width=120)  # 创建绘图板   电阻
        # self.canvas_show_capacitor = tkinter.Canvas(self.root,  height=50, width=120)  # 创建绘图板   电容
        # self.canvas_show_information = tkinter.Canvas(self.root, height=100, width=250)       #信息显示栏
        # self.canvas_write = tkinter.Canvas(self.root, height=900, width=200)  # 创建绘图板


        self.canvas_show_inductor.create_text(200,50,  text="请选择器件信息：",fill="yellow", font=("微软雅黑", 12))

        self.image_inductor = tkinter.PhotoImage(file=INDUCTOR_PATH)  # 底图对象
        self.canvas_show_inductor.create_image((0, 0), anchor=tkinter.NW)  # 图像

        self.image_resistor = tkinter.PhotoImage(file=RESISTOR_PATH)  # 底图对象
        self.canvas_show_resistor.create_image((0, 0), anchor=tkinter.NW)  # 图像

        self.image_capacitor = tkinter.PhotoImage(file=CAPACITOR_PATH)  # 底图对象
        self.canvas_show_capacitor.create_image((0, 0), anchor=tkinter.NW, image=self.image_capacitor)  # 图像

        self.canvas_write.create_rectangle(60, 70, 20, 50, fill="yellow")  # 矩形
        self.canvas_write.create_text(40, 30, text="画布",
                                      fill="red", font=("微软雅黑", 20))  # 文字
        self.canvas_show_inductor.pack(side='top',  fill="x")  # 画布显示
        self.canvas_show_resistor.pack(side='top',  fill="x")  # 画布显示
        self.canvas_show_capacitor.pack( side ="top", fill="x")  # 画布显示
        self.canvas_show_information.pack(side="left", fill="both")  # 画布显示
        #grid布局
        # self.canvas_show_inductor.grid(row=0, column=0)
        # self.canvas_show_resistor.grid(row=0, column=1)
        # self.canvas_show_capacitor.grid(row=0, column=2)

        self.canvas_write.pack(side='right', expand='yes', fill='both')  # 画布显示


    def button(self):

        # self.image_inductor = tkinter.PhotoImage(file=INDUCTOR_PATH)  # 底图对象
        self.button_inductor = tkinter.Button(self.canvas_show_information, height=80, width=150  ,text="电感", image=self.image_inductor,
                                          compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_inductor.bind("<Button-1>", lambda event: self.event_handle(event))  # 事件处理
        self.button_inductor.pack(side='top', anchor='sw',padx=5, pady=5)  # 按钮显示

        self.button_resistor = tkinter.Button(self.canvas_show_information,height=80, width=150 , text="电阻", image=self.image_resistor,
                                         compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_resistor.pack(side='top', anchor='sw',padx=5, pady=5)  # 按钮显示

        self.button_capacitor = tkinter.Button(self.canvas_show_information,height=80, width=150  , text="电容", image=self.image_capacitor,
                                          compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_capacitor.pack(side='top', anchor='sw',padx=5, pady=5)  # 按钮显示

    def combobox(self):

        self.frame = tkinter.Frame(self.canvas_show_inductor)  # 创建Frame
        tkinter.Label(self.frame, text="请选择器件：", font=("微软雅黑", 8),
                      justify="left").grid(row=0, column=0, sticky=tkinter.W)  # 显示标签
        city_tuple = ("电阻", "电容", "电感", "电源")  # 下拉项
        self.city_combobox = tkinter.ttk.Combobox(self.frame, values=city_tuple)  # 列表项
        self.city_combobox.bind("<<ComboboxSelected>>", self.show_data)  # 选项改变
        self.city_combobox.grid(row=0, column=1)  # 显示组件
        self.frame.pack(side="left",anchor='nw',padx=5, pady=5)  # Frame显示
        self.content = tkinter.StringVar()  # 修改内容
        self.label = tkinter.Label(self.canvas_write, textvariable=self.content, width=500,
                                   height=50, font=("微软雅黑", 20), justify="right")  # 标签
        self.label.pack()  # 显示标签


    def show_data(self, event):  # 事件处理
        self.content.set("选择器件：%s" % self.city_combobox.get())  # 内容显示


    def motion_handle(self, event): 				# 事件处理函数

        self.label.place(x=event.x_root, y=event.y_root) 			# 组件重新定位

    def my_text(self):

        self.photo = tkinter.PhotoImage(file=LOGO_PATH)  # 图片
        self.label = tkinter.Label(self.canvas_show_inductor, image=self.photo)  # 标签
        self.label.bind("<B1-Motion>", self.motion_handle)  # 鼠标左键拖动
        self.label.pack()  # 显示标签


        # label_text = tkinter.Label(self.canvas_show_capacitor,text="陈灿：",
        #                             bg="#223011",
        #                            font=("微软雅黑", 20), fg="#ffffff", justify="right")
        # text = tkinter.Text(self.canvas_show_capacitor,width=50, height=5, font=("微软雅黑", 10))
        # text.insert("current", "请输入：")
        # text.pack()
        # label_text.pack()  # 显示文字

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

    def src_listbox(self):  # 定义列表
        self.language_label = tkinter.Label(self.canvas_show_information, text="请选择你需要的器件规格：",
                                            bg="#223011", font=("微软雅黑", 9), fg="#ffffff", justify="left")  # 提示信息
        self.language_label.pack()  # 组件显示
        self.language_list = ["20Ω", "50Ω", "100Ω"]  # 候选列表
        self.language_listbox = tkinter.Listbox(self.canvas_show_information, selectmode="multiple")  # 列表项
        for item in self.language_list:  # 循环添加
            self.language_listbox.insert("end", item)  # 列表内容
        self.language_listbox.bind("<Double-Button-1>", self.change_item_handle)  # 双击修改
        self.language_listbox.pack()

    def dest_listbox(self):  # 定义列表
        self.choose_label = tkinter.Label(self.canvas_write, text="请画出你的电路：", bg="#223011",
                                          font=("微软雅黑", 9), fg="#ffffff", justify="left")  # 提示信息
        self.choose_label.pack()  # 组件显示
        self.choose_listbox = tkinter.Listbox(self.canvas_write,
                                              selectmode="multiple")  # 列表项，多选模式
        self.choose_listbox.pack()  # 组件显示

    #  列表修改
    def change_item_handle(self, event):
        for index in self.language_listbox.curselection():  # 获取选定项索引
            self.choose_listbox.insert("end",
                                       self.language_listbox.get(index))  # 保存新增项
        while True:  # 循环处理
            if self.language_listbox.curselection():  # 找到选中项
                self.language_listbox.delete(
                    self.language_listbox.curselection()[0])  # 删除列表项
            else:  # 没有选中项
                break  # 结束循环
    #显示操作的button
    def oper_button(self):  # 事件处理函数
        self.add_button = tkinter.Button(self.canvas_show_information, text="添加>>",
                                         fg="black", font=("微软雅黑", 10))  # 批量操作按钮
        self.add_button.bind("<Button-1>", self.change_item_handle)  # 事件绑定
        self.add_button.pack()  # 组件显示


        #窗体关闭监听
    def close_handle(self):  # 事件处理函数
        if tkinter.messagebox.askyesnocancel("程序关闭确认", "这么好的程序真舍得关闭吗？？"):
            self.root.destroy()  # 关闭程序



def main():							# 主函数
    MainForm()							# 显示主窗体

if __name__ == "__main__":     					# 判断执行名称
    main()							# 调用主函数



