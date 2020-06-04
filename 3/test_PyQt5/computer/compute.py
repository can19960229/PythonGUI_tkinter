# -*- coding: utf-8 -*-
# @Time : 2019/12/4 9:20
# @Author :
# @Site :
# @File : main.py
# @Software: PyCharm
import sys
from PyQt5 import QtCore


from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from mycalc import Ui_MainWindow


class CalcSignal(QObject):
    """
        自定义信号
    """
    signal_number = pyqtSignal(int)
    signal_method = pyqtSignal(str)
    signal_clear = pyqtSignal(int)
    signal_result = pyqtSignal()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.first_number = 0
        self.method = ''
        self.sec_number = 0
        self.is_get_result = 0
        self.mysignal = CalcSignal()
        # 绑定信号和槽
        self.mysignal.signal_number.connect(self.deal_number)
        self.mysignal.signal_method.connect(self.deal_method)
        self.mysignal.signal_clear.connect(self.deal_clear)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText('0')
        self.ui.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self._init_button()

    def _init_button(self):
        """
        初始化所有的button click事件绑定对应的回调函数
        :return:
        """
        # 设置按钮
        self.ui.zero.clicked.connect(self.num_click)
        self.ui.one.clicked.connect(self.num_click)
        self.ui.two.clicked.connect(self.num_click)
        self.ui.three.clicked.connect(self.num_click)
        self.ui.four.clicked.connect(self.num_click)
        self.ui.five.clicked.connect(self.num_click)
        self.ui.six.clicked.connect(self.num_click)
        self.ui.seven.clicked.connect(self.num_click)
        self.ui.eight.clicked.connect(self.num_click)
        self.ui.nine.clicked.connect(self.num_click)

        self.ui.point.clicked.connect(self.deal_point)
        # 计算方法
        self.ui.add.clicked.connect(self.method_click)
        self.ui.sub.clicked.connect(self.method_click)
        self.ui.multi.clicked.connect(self.method_click)
        self.ui.division.clicked.connect(self.method_click)
        # 结果
        self.ui.result.clicked.connect(self.deal_result)
        # 清空按钮
        self.ui.clear_all.clicked.connect(self.clear_click)
        self.ui.myclear.clicked.connect(self.clear_click)

    def num_click(self):
        """触发数字按钮信号"""
        number = self.sender()
        self.mysignal.signal_number.emit(int(number.text()))

    def method_click(self):
        """触发运算符信号"""
        method = self.sender().text()
        self.mysignal.signal_method.emit(method)

    def clear_click(self):
        """触发清空信号"""
        clear = self.sender().text()
        if clear == 'C':
            self.mysignal.signal_clear.emit(1)
        else:
            self.mysignal.signal_clear.emit(0)

    def deal_number(self, val):
        """
        点击数字回调函数
        :param val:
        :return:
        """
        temp = self.ui.lineEdit.text()
        if temp in ['+', '-', '*', '/']:
            self.ui.lineEdit.setText(str(val))
        else:
            if temp.find('.') == -1:
                temp = self.ui.lineEdit.text().lstrip('0')
            self.ui.lineEdit.setText(temp + str(val))

    def deal_method(self, val):
        """
        加减乘除运算处理回调
        :param val:
        :return:
        """
        temp = self.ui.lineEdit.text()
        if self.method == '':
            if temp not in ['+', '-', '*', '/']:
                self.first_number = eval(temp)
        else:
            if temp not in ['+', '-', '*', '/']:
                self.sec_number = eval(self.ui.lineEdit.text())
                if self.method == '+':
                    self.first_number = self.first_number + self.sec_number
                elif self.method == '-':
                    self.first_number = self.first_number - self.sec_number
                elif self.method == '*':
                    self.first_number = self.first_number * self.sec_number
                else:
                    if self.sec_number != 0:
                        self.first_number = self.first_number / self.sec_number
                self.sec_number = 0
        self.method = val
        self.ui.lineEdit.setText(val)

    def deal_clear(self, val):
        """
        两种清空回调函数
        :param val:
        :return:
        """
        if val:
            self.first_number = 0
            self.method = ''
            self.sec_number = 0
            self.ui.lineEdit.setText('0')
        else:
            if self.sec_number == 0 and self.method == '' and self.first_number != 0:
                self.first_number = 0
                self.ui.lineEdit.setText('0')
            elif self.sec_number == 0 and self.method != '':
                self.ui.lineEdit.setText('0')
            elif self.sec_number != 0:
                self.sec_number = 0
                if self.method != '':
                    self.ui.lineEdit.setText(self.method)
                else:
                    self.ui.lineEdit.setText('0')
            else:
                self.ui.lineEdit.setText('0')

    def deal_result(self):
        """
        处理等号事件
        :return:
        """
        temp = self.ui.lineEdit.text()
        if temp in ['+', '-', '*', '/']:
            self.method = ''
            self.sec_number = 0
            self.ui.lineEdit.setText(str(self.first_number))
            self.first_number = 0
            return
        self.sec_number = eval(temp)
        if self.method == '':
            result = eval(temp)
        elif self.method == '+':
            result = self.first_number + self.sec_number
        elif self.method == '-':
            result = self.first_number - self.sec_number
        elif self.method == '*':
            result = self.first_number * self.sec_number
        else:
            if self.sec_number != 0:
                result = self.first_number / self.sec_number
            else:
                result = 0
                print('除数不能为0')
                self.alert()
        self.method = ''
        self.sec_number = 0
        self.first_number = result
        self.ui.lineEdit.setText(str(result))

    def alert(self):
        """
        除数为0时重置所有，并弹框
        :return:
        """
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(u'提示')
        msgBox.setText(u"除数不能为0")
        msgBox.setWindowIcon(QIcon('./favicon.ico'))

        # 隐藏ok按钮
        msgBox.addButton(QMessageBox.Ok)
        msgBox.button(QMessageBox.Ok).hide()

        # 模态对话框
        msgBox.exec_()

    def deal_point(self):
        """
        小数点事件
        :return:
        """
        temp = self.ui.lineEdit.text()
        if temp in ['+', '-', '*', '/']:
            self.ui.lineEdit.setText('0.')
        else:
            tempindex = temp.find('.')
            if tempindex == -1:
                self.ui.lineEdit.setText(temp + '.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowIcon(QIcon('./favicon.ico'))
    main_window.setWindowTitle('我的计算器')
    main_window.setFixedSize(560, 450)
    main_window.show()
    app.exec()