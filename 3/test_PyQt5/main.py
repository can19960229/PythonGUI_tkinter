import sys
import test
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':  # import到其他的python脚本中被调用（模块重用）执行,sys.argv就是运行程序时候获取命令行参数
    app = QApplication(sys.argv)  # 创建了一个QApplication对象，对象名为app，带两个参数sys.argv
    MainWindow = QMainWindow()  # 创建主窗口程序，将QMainWindow()类赋给对象MainWindow
    ui = test.Ui_MainWindow()  # 将Ui_MainWindows()类赋给对象ui
    ui.setupUi(MainWindow)  # 调用函数setupUi()
    MainWindow.show()  # 显示窗口
    sys.exit(app.exec_())  # app.exet_()程序一直循环运行直到主窗口被关闭终止进程