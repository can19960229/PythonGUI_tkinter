import tkinter


class show_canvas_write(object):
    def __init__(self,master = None):
        self.root = master  #定义内部变量root
   
        self.show_canvas_mywrite()
        
    #获取参数：创建的画布3
    def get_canvas_writeParam(self):
        print("获取了这个函数")
        # return self.canvas_write


    def show_canvas_mywrite(self):
        print("获取了这个----创建我的write画布-----------的函数")
        self.canvas_write = tkinter.Canvas(self.root,bg='green', height=880, width=800)  # 创建绘图板

     
        self.canvas_write.create_rectangle(60, 70, 20, 50, fill="yellow")  # 矩形
        self.canvas_write.create_text(40, 30, text="画布",
                                      fill="red", font=("微软雅黑", 20))  # 文字

        self.canvas_write.pack(side='right', expand='yes', fill='both')  # 画布显示

        # grid布局
        # self.canvas_show_inductor.grid(row=0, column=0)
        # self.canvas_show_resistor.grid(row=0, column=1)
        # self.canvas_show_capacitor.grid(row=0, column=2)


