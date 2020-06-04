from tkinter import *
from show_canvas import *

class MainForm(show_canvas):

    def __init__(self):
        self.myinit()


    def myinit(self):

       self.root = tkinter.Tk()  # 创建窗体
       self.root.title("这是一个界面")  # 设置窗体标题
       self.root.geometry("1000x1000")  # 设置主窗体大小
       self.root.maxsize(1000, 1000)  # 设置窗体最大尺寸
       self.root["background"] = "LightSlateGray"  # 设置背景颜色

       self.root.mainloop()


if __name__ == '__main__':
    MainForm()


    # show_canvas.show_mycanvas()  # 进行登录界面的实现


