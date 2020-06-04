import tkinter
from show_canvas_nemu import *
from show_canvas_information import *
from show_canvas_write import *


class show_canvas:
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("1000x1000")  # 设置主窗体大小
        self.root.maxsize(1000, 1000)  # 设置窗体最大尺寸
        self.root["background"] = "LightSlateGray"  # 设置背景颜色
        
        self.show_mycanvas()

    def show_mycanvas(self):
        # show_canvas_nemu()

        self.canvas_show_nemu = tkinter.Canvas(self.root, bg='red', height=120, width=1000)  # 创建绘图板 电感

        self.canvas_show_nemu.create_text(500, 50, text="请选择器件信息：", fill="yellow", font=("微软雅黑", 12))

        self.canvas_show_nemu.pack(side='top', fill='x')  # 画布显示

        # show_canvas_information()

        self.canvas_show_information = tkinter.Canvas(self.root, bg='yellow', height=880, width=200)  # 信息显示栏
        self.canvas_show_information.pack(side='left', expand='no', fill='y')  # 画布显示

        # show_canvas_write()

        self.canvas_write = tkinter.Canvas(self.root, bg='green', height=880, width=800)  # 创建绘图板

        self.canvas_write.create_rectangle(60, 70, 20, 50, fill="yellow")  # 矩形
        self.canvas_write.create_text(40, 30, text="画布",
                                      fill="red", font=("微软雅黑", 20))  # 文字

        self.canvas_write.pack(side='right', expand='yes', fill='both')  # 画布显示

        