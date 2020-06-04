import tkinter

class Increat_Canvas:
    def __init__(self):
        self.root = tkinter.Tk()  # 创建窗体
        self.root.title("这是一个界面")  # 设置窗体标题
        self.root.geometry("1000x1000")  # 设置主窗体大小
        self.root.maxsize(1000, 1000)  # 设置窗体最大尺寸
        self.root["background"] = "LightSlateGray"  # 设置背景颜色

    def capacitor(canvas, x, y, xlen, ylen):
        if xlen >= ylen:
            xd = xlen / 10;
            yd = ylen / 2;
            canvas.create_line(x, y, x + 4 * xd, y, width=1)
            canvas.create_line(x + 4 * xd, y - yd, x + 4 * xd, y + yd, width=1)
            canvas.create_line(x + 5 * xd, y - yd, x + 5 * xd, y + yd, width=1)
            canvas.create_line(x + 5 * xd, y, x + 10 * xd, y, width=1)
        else:
            xd = xlen / 2;
            yd = ylen / 10;
            canvas.create_line(x, y, x, y + 4 * yd, width=1)
            canvas.create_line(x - xd, y + 4 * yd, x + xd, y + 4 * yd, width=1)
            canvas.create_line(x - xd, y + 5 * yd, x + xd, y + 5 * yd, width=1)
            canvas.create_line(x, y + 5 * yd, x, y + 10 * yd, width=1)
        return

    def resistor(canvas, x, y, xlen, ylen):
        if xlen > ylen:
            xd = xlen / 10;
            yd = ylen / 2;
            canvas.create_line(x, y, x + 3 * xd, y, width=1)
            canvas.create_rectangle(x + 3 * xd, y - yd, x + 6 * xd, y + yd)
            canvas.create_line(x + 6 * xd, y, x + 10 * xd, y, width=1)
        else:
            xd = xlen / 2;
            yd = ylen / 10;
            canvas.create_line(x, y, x, y + 3 * yd, width=1)
            canvas.create_rectangle(x - xd, y + 3 * yd, x + xd, y + 6 * yd)
            canvas.create_line(x, y + 6 * yd, x, y + 10 * yd, width=1)
        return

    def inductor(canvas, x, y, xlen, ylen):
        if xlen >= ylen:
            xd = xlen / 10
            yd = ylen / 2
            canvas.create_line(x, y, x + 3 * xd, y, width=1)
            canvas.create_arc(x + 3 * xd, y - yd, x + 4 * xd, y + yd, start=0, extent=180, style=ARC)
            canvas.create_arc(x + 4 * xd, y - yd, x + 5 * xd, y + yd, start=0, extent=180, style=ARC)
            canvas.create_arc(x + 5 * xd, y - yd, x + 6 * xd, y + yd, start=0, extent=180, style=ARC)
            canvas.create_line(x + 6 * xd, y, x + 10 * xd, y, width=1)
        else:
            xd = xlen / 2
            yd = ylen / 10
            canvas.create_line(x, y, x, y + 3 * yd, width=1)
            canvas.create_arc(x - xd, y + 3 * yd, x + xd, y + 4 * yd, start=-90, extent=180, style=ARC)
            canvas.create_arc(x - xd, y + 4 * yd, x + xd, y + 5 * yd, start=-90, extent=180, style=ARC)
            canvas.create_arc(x - xd, y + 5 * yd, x + xd, y + 6 * yd, start=-90, extent=180, style=ARC)
            canvas.create_line(x, y + 6 * yd, x, y + 10 * yd, width=1)
        return

    def point(canvas, x, y, r):
        canvas.create_oval(x - r, y - r, x + r, y + r, fill='black')
        return

