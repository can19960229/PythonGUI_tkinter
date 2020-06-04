import tkinter
import tkinter.messagebox
from component_info import ComponentInfo
from component_creat import CreatComponent


C_PATH = "D:\\chencan\\python\\PYECourse\\3\\venv\\resource\\2.png"
R_PATH = "D:\\chencan\\python\\PYECourse\\3\\venv\\resource\\1.png"
L_PATH = "D:\\chencan\\python\\PYECourse\\3\\venv\\resource\\3.png"

class MainForm:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("小小窗体")
        self.root.geometry('500x500')
        self.root.maxsize(width=1500,height=1000)
        self.root["background"] = "green"
        #############调用函数##############
        self.showCanvas()
        self.addLabel()
        self.getEntry()
        self.addButton()
        ############循环中计数##############
        self.num_i = tkinter.IntVar
        self.num_i = 1

        self.root.mainloop()

    def showCanvas(self):            #显示画布
        self.canvas_1 = tkinter.Canvas(width=500,height=50,bg="red")
        self.canvas_1.pack(side='top',expand='no',fill='x')

        self.canvas_2 = tkinter.Canvas(width=100,height=100,bg='yellow')
        self.canvas_2.pack(side='left',anchor='nw',fill='y')

        self.canvas_3 = tkinter.Canvas(bg='grey')
        self.canvas_3.pack(side='left',expand='yes',fill='both')

#############     canvas_1    ##############################
    def addLabel(self):
        self.Label1 = tkinter.Label(self.canvas_1,width=35,foreground='blue',text='Input information：C/L/R-xx-xxx-xxx-xxx')
        self.Label1.pack(side='left')
            #############文  本   框   输   入##############################
    def getEntry(self):
        self.input_var = tkinter.StringVar()
        self.inputEntry = tkinter.Entry(self.canvas_1,textvariable=self.input_var)
        self.inputEntry.pack(side='left')

        self.getEntry_Button()

    def getEntry_Button(self):  # 按钮确认获取成功文本框内容
        self.sure_Button = tkinter.Button(self.canvas_1, text='ok')
        self.sure_Button.bind("<Button-1>", self.Analysis_Creat)
        self.sure_Button.pack(side='left')

            ##########解析文本  并  创建元件###########################
    def Analysis_Creat(self,event):     #解析文本框内容，创建元器件
        self.info = self.input_var.get().split('-')  # 将字符串以‘-’分隔开，放到数组当中

        # self.ComList = tkinter.Listbox(root,listvariable=item)
        self.move_canvas = tkinter.Canvas(self.canvas_3,width=100,height=100,bg='white')

        if self.info[0] == 'C':
            self.components = CreatComponent.capacitor(self.move_canvas,x=20,y=20,xlen=100,ylen=20)
            self.move_canvas.pack(side='top', anchor='nw')
            # self.info_lable_No = tkinter.Label(self.move_canvas, text=self.component_info.No)
            # self.info_lable_No.place(x=0,y=0)
            self.move_canvas.bind("<B1-Motion>", self.MoveComponent)
            self.move_canvas.bind('<Button-3>',self.RightClickMenu)
            self.move_canvas.bind('<Double-Button-1>',self.doubleClick)

        elif self.info[0] == 'R':
            self.components = CreatComponent.resistor(self.move_canvas,x=20,y=20,xlen=100,ylen=20)
            self.move_canvas.pack(side='top', anchor='nw')
            self.move_canvas.bind("<B1-Motion>", self.MoveComponent)
            self.move_canvas.bind('<Button-3>',self.RightClickMenu)
            self.move_canvas.bind('<Double-Button-1>',self.doubleClick)

        elif self.info[0] == 'L':
            self.components = CreatComponent.inductor(self.move_canvas,x=20,y=20,xlen=100,ylen=20)
            self.move_canvas.pack(side='top', anchor='nw')
            self.move_canvas.bind("<B1-Motion>", self.MoveComponent)
            self.move_canvas.bind('<Button-3>',self.RightClickMenu)
            self.move_canvas.bind('<Double-Button-1>',self.doubleClick)

        else:
            result = tkinter.messagebox.showwarning(title='警告',message='请输入正确格式')

        self.component_info = ComponentInfo()
        self.component_info.type  = self.info[0]
        self.component_info.No    = self.info[1]
        self.component_info.x     = self.info[2]
        self.component_info.y     = self.info[3]
        self.component_info.value = self.info[4]


    def MoveComponent(self,event):
        self.move_canvas.place(x=event.x_root, y=event.y_root) 			# 组件重新定位

    def RightClickMenu(self,event):
        self.menu = tkinter.Menu(self.canvas_3)
        self.menu.add_cascade(label='旋转')
        self.menu.post(event.x_root, event.y_root)

    def doubleClick(self,event):
        ComponentInfo.showComponent_info()
        # result = tkinter.messagebox.askokcancel(title='信息',message='111111')

########################canvas   2   ##################################
    def addButton(self):
        photo_C = tkinter.PhotoImage(file=C_PATH)
        self.button_show_R = tkinter.Button(self.canvas_2,width=100,height=50,image=photo_C).pack(side='top')
        photo_R = tkinter.PhotoImage(file=R_PATH)
        self.button_show_R = tkinter.Button(self.canvas_2,width=100,height=50,image=photo_R).pack(side='top')
        photo_L = tkinter.PhotoImage(file=L_PATH)
        self.button_show_R = tkinter.Button(self.canvas_2,width=100,height=50,image=photo_L).pack(side='top')

    def OK_getEntry(self,event): #打印文本框内容，用以监测
        # print("1")
        print(self.input_var.get())     #将文本框中的内容获取到input_var中，打印
        print(self.input_var.get().split('-'))          #打印，将字符串以‘-’分隔开，放到数组当中
        print(self.info_x)             #获取数组中的第一位


if __name__ == "__main__":  # 判断执行名称
    MainForm()