import tkinter

class CreatComponent:  						# 定义主窗体类
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

    def resistor(canvas, x, y, xlen, ylen):
        if xlen > ylen:
            xd = xlen / 10;
            yd = ylen / 2;
            canvas.create_line(x, y, x+3*xd, y, width=1)
            canvas.create_rectangle(x + 3*xd, y-yd, x+6*xd, y+yd)
            canvas.create_line(x+6*xd, y, x+10*xd, y, width=1)
        else:
            xd = xlen / 2;
            yd = ylen / 10;
            canvas.create_line(x, y, x, y+3*yd, width=1)
            canvas.create_rectangle(x-xd, y+3*yd, x+xd, y+6*yd)
            canvas.create_line(x, y+6*yd, x, y+10*yd, width=1)
        return

    def inductor(canvas,x,y,xlen,ylen):
        if xlen>=ylen :
            xd=xlen/10
            yd=ylen/2
            canvas.create_line(x,y,x+3*xd,y,width=1)
            canvas.create_arc(x+3*xd,y-yd,x+4*xd,y+yd,start=0,extent=180,style=tkinter.ARC)
            canvas.create_arc(x+4*xd,y-yd,x+5*xd,y+yd,start=0,extent=180,style=tkinter.ARC)
            canvas.create_arc(x+5*xd,y-yd,x+6*xd,y+yd,start=0,extent=180,style=tkinter.ARC)
            canvas.create_line(x+6*xd,y,x+10*xd,y,width=1)
        else:
            xd=xlen/2
            yd=ylen/10
            canvas.create_line(x,y,x,y+3*yd,width=1)
            canvas.create_arc(x-xd,y+3*yd,x+xd,y+4*yd,start=-90,extent=180,style=tkinter.ARC)
            canvas.create_arc(x-xd,y+4*yd,x+xd,y+5*yd,start=-90,extent=180,style=tkinter.ARC)
            canvas.create_arc(x-xd,y+5*yd,x+xd,y+6*yd,start=-90,extent=180,style=tkinter.ARC)
            canvas.create_line(x,y+6*yd,x,y+10*yd,width=1)
        return
    
    def myline(canvas,x,y,xlen,ylen):
        if xlen > ylen:
            xd = xlen / 10;
            yd = ylen / 2;
            canvas.create_line(x, y, x+5*xd, y, width=1)
        else:
            xd = xlen / 2;
            yd = ylen / 10;
            canvas.create_line(x, y, x, y+5*yd, width=1)

    def point(canvas,x,y,r):
        canvas.create_oval(x-r,y-r,x+r,y+r,fill='black')
        return

    def Dotframe(canvas, x, y, xlen, ylen):
        if xlen >= ylen:
            xd = xlen / 10
            yd = ylen / 2
            canvas.create_line(x, y, x + 5 * xd, y, width=1)

            canvas.create_rectangle(x + 5 * xd, y - 3*yd, x + 20 * xd, y + 3*yd ,dash = 10,outline = '#ccbbaa',width=5,
                    fill = '#fddccf')
            # canvas.create_line(x + 5 * xd, y - 3 * yd, x + 5 * xd, y + 3 * yd, width=1, dash=(4, 4))
            # canvas.create_line(x + 5 * xd, y - 3 * yd, x + 20 * xd, y - 3 * yd, width=1, dash=(4, 4))
            # canvas.create_line(x + 20 * xd, y - 3 * yd, x + 20 * xd, y + 3 * yd, width=1, dash=(4, 4))
            # canvas.create_line(x + 5 * xd, y + 3 * yd, x + 20 * xd, y + 3 * yd, width=1, dash=(4, 4))
            canvas.create_line(x + 20 * xd, y, x + 25 * xd, y, width=1)
        else:
            xd = xlen / 2
            yd = ylen / 10
            canvas.create_line(x, y, x, y + 5 * xd, width=1)
            canvas.create_rectangle(x - 3 * xd, y + 5 * yd, x + 3 * xd, y + 20 * yd, dash=4,outline = '#ccbbaa',width=5,
                    fill = '#fddccf')
            # canvas.create_line(x - 3 * xd, y + 5 * yd, x + 3 * xd, y + 5 * yd, width=1, dash=(4, 4))
            # canvas.create_line(x - 3 * xd, y + 5 * yd, x - 3 * xd, y + 20 * yd, width=1, dash=(4, 4))
            # canvas.create_line(x - 3 * xd, y + 20 * yd, x + 3 * xd, y + 20 * yd, width=1, dash=(4, 4))
            # canvas.create_line(x + 3 * xd, y + 5 * yd, x + 3 * xd, y + 20 * yd, width=1, dash=(4, 4))
            canvas.create_line(x, y + 20 * yd, x, y + 25 * yd, width=1)

    def show_create_text(canvas,x,y,num):
        canvas.create_text(x, y, text="%s:" % num, font=("微软雅黑", 12))


    # 为鼠标点击事件绑定事件处理函数

    # def click_handler(self,event):
    #     self.point(self.canvas,event.x,event.y,4)
    #     return
    # 
    # def drag(self,event):
    #     self.cap1.place(x=event.x,y=event.y)
