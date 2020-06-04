import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


win = tkinter.Tk()
win.title("鼠标拖动事件")
win.geometry("800x600+600+100")

# <B1-Motion> 拖动左键触发事件
# <B2-Motion> 拖动中键触发事件
# <B3-Motion> 拖动右键触发事件

label = tkinter.Label(win, text="red orange yellow green cyan blue violet拖动鼠标打印")
label.pack()

can =tkinter.Canvas(win,width=100,height=100,bg="green")    #意为拖动此幕布
can.pack()

def func(event):
    print(event.x, event.y)

def mousePressEvent(self, event):
    if event.buttons() == Qt.LeftButton:
        self.setCursor(Qt.OpenHandCursor)
        self.parent.m_drag = True
        self.parent.m_DragPosition = event.globalPos() - self.parent.pos()
        event.accept()


def mouseMoveEvent(self, event):
    try:
        if event.buttons() and Qt.LeftButton:
            self.parent.move(event.globalPos() - self.parent.m_DragPosition)  # move将窗口移动到指定位置
            event.accept()
            self.parent.move()
    except AttributeError:
        pass


def mouseReleaseEvent(self, event):
    print("1")
    if event.button() == Qt.LeftButton:
        self.m_drag = False
        self.unsetCursor()


# can.bind("<B1-Motion>", func)
can.bind("<B1-Motion>",mouseReleaseEvent)

win.mainloop()