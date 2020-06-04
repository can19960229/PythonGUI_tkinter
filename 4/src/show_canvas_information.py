import tkinter, os	,tkinter.messagebox,tkinter.simpledialog,tkinter.ttk
from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
from tkinter.messagebox import showinfo, showwarning, showerror


from show_canvas_write import *

class show_canvas_information(object):
    def __init__(self,master = None):
        self.root = master  #定义内部变量root

        self.show_canvas_myinformation()
        self.show_button_capacitor()
        self.show_button_inductor()
        self.show_button_resistor()

    def show_canvas_myinformation(self):
        self.canvas_show_information = tkinter.Canvas(self.root,bg='yellow',height=880, width=200)       #信息显示栏
        self.canvas_show_information.pack(side='left', expand='no', fill='y')  # 画布显示

        # grid布局
        # self.canvas_show_inductor.grid(row=0, column=0)
        # self.canvas_show_resistor.grid(row=0, column=1)
        # self.canvas_show_capacitor.grid(row=0, column=2)

    def show_button_inductor(self):
        # self.image_inductor = tkinter.PhotoImage(file=INDUCTOR_PATH)  # 底图对象
        self.button_inductor = tkinter.Button(self.canvas_show_information, height=2, width=10, text="电感",
                                              # image=self.image_inductor,
                                              compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_inductor.pack(side='top', anchor='sw', padx=5, pady=5)  # 按钮显示
        self.button_inductor.bind("<Button-1>", lambda event: self.event_handle(event))  # 事件处理

    def show_button_resistor(self):
        self.button_resistor = tkinter.Button(self.canvas_show_information, height=2, width=10, text="电阻",
                                              # image=self.image_resistor,
                                              compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_resistor.pack(side='top', anchor='sw', fill='x', padx=5, pady=5)  # 按钮显示

    def show_button_capacitor(self):
        self.button_capacitor = tkinter.Button(self.canvas_show_information, height=2, width=10, text="电容",
                                               # image=self.image_capacitor,
                                               compound="bottom", fg="black", font=("微软雅黑", 10))  # 定义按钮
        self.button_capacitor.pack(side='top', anchor='sw', padx=5, pady=5)  # 按钮显示
    
    def event_handle(self, event):  # 事件处理函数
        input_message = tkinter.simpledialog.askstring("提示信息", "请输入要显示的信息：")

        # label_text = tkinter.Label(self.canvas_write, text=input_message,bg="#223011", font=("微软雅黑", 10),
        #                            fg="#ffffff", justify="right")  # 创建标签

        label_text = tkinter.Label( ######需要获得write中的get_canvas_write的画布
                                    self.get_canvaswrite(show_canvas_write()),
                                    text=input_message, bg="#223011", font=("微软雅黑", 10),
                                   fg="#ffffff", justify="right")  # 创建标签

        
        label_text.pack()  # 组件显示

    def get_canvaswrite(self,canvas_write):
        canvas_write.get_canvas_writeParam()

