from tkinter import *

def capacitor(canvas,x,y,xlen,ylen):
    if xlen>=ylen:
        xd=xlen/10;
        yd=ylen/2;
        canvas.create_line(x,y,x+4*xd,y,width=1)
        canvas.create_line(x+4*xd,y-yd,x+4*xd,y+yd,width=1)
        canvas.create_line(x+5*xd,y-yd,x+5*xd,y+yd,width=1)
        canvas.create_line(x+5*xd,y,x+10*xd,y,width=1)
    else:
        xd=xlen/2;
        yd=ylen/10;
        canvas.create_line(x,y,x,y+4*yd,width=1)
        canvas.create_line(x-xd,y+4*yd,x+xd,y+4*yd,width=1)
        canvas.create_line(x-xd,y+5*yd,x+xd,y+5*yd,width=1)
        canvas.create_line(x,y+5*yd,x,y+10*yd,width=1)
    return

def resistor(canvas,x,y,xlen,ylen):
    if xlen>ylen:
        xd=xlen/10;
        yd=ylen/2;
        canvas.create_line(x,y,x+3*xd,y,width=1)
        canvas.create_rectangle(x+3*xd,y-yd,x+6*xd,y+yd)
        canvas.create_line(x+6*xd,y,x+10*xd,y,width=1)
    else:
        xd=xlen/2;
        yd=ylen/10;
        canvas.create_line(x,y,x,y+3*yd,width=1)
        canvas.create_rectangle(x-xd,y+3*yd,x+xd,y+6*yd)
        canvas.create_line(x,y+6*yd,x,y+10*yd,width=1)            
    return
def inductor(canvas,x,y,xlen,ylen):
    if xlen>=ylen :
        xd=xlen/10
        yd=ylen/2
        canvas.create_line(x,y,x+3*xd,y,width=1)
        canvas.create_arc(x+3*xd,y-yd,x+4*xd,y+yd,start=0,extent=180,style=ARC)
        canvas.create_arc(x+4*xd,y-yd,x+5*xd,y+yd,start=0,extent=180,style=ARC)
        canvas.create_arc(x+5*xd,y-yd,x+6*xd,y+yd,start=0,extent=180,style=ARC)
        canvas.create_line(x+6*xd,y,x+10*xd,y,width=1)
    else:
        xd=xlen/2
        yd=ylen/10
        canvas.create_line(x,y,x,y+3*yd,width=1)
        canvas.create_arc(x-xd,y+3*yd,x+xd,y+4*yd,start=-90,extent=180,style=ARC)
        canvas.create_arc(x-xd,y+4*yd,x+xd,y+5*yd,start=-90,extent=180,style=ARC)
        canvas.create_arc(x-xd,y+5*yd,x+xd,y+6*yd,start=-90,extent=180,style=ARC)
        canvas.create_line(x,y+6*yd,x,y+10*yd,width=1)
    return
def point(canvas,x,y,r):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill='black')
    return



window1=Tk()
window1.title('test2')
canvas1=Canvas(window1,width=400,height=400,bg='red')  # 设置画布
canvas1.pack()  # 显示画布
# 利用create_line()在画布上绘制直线
capacitor(canvas1,100,100,20,100)
capacitor(canvas1,100,80,100,20)
resistor(canvas1,200,40,100,20)
resistor(canvas1,200,100,20,100)
inductor(canvas1,40,40,100,20)
inductor(canvas1,40,60,20,100)
point(canvas1,40,60,4)

# 为鼠标点击事件绑定事件处理函数
def click_handler(event):
    point(canvas1,event.x,event.y,4)
    return
canvas1.bind('<Button-1>', click_handler)

window1.mainloop()
