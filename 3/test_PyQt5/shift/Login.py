# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\python UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow_Login(object):
    def setupUi(self, SelectComponents):
        SelectComponents.setObjectName("Check The Answer")
        SelectComponents.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(SelectComponents)
        self.pushButton.setGeometry(QtCore.QRect(130, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SelectComponents)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 250, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(SelectComponents)
        self.label.setGeometry(QtCore.QRect(140, 80, 72, 15))
        self.label.setObjectName("label")

        self.retranslateUi(SelectComponents)
        QtCore.QMetaObject.connectSlotsByName(SelectComponents)

    def retranslateUi(self, SelectComponents):
        _translate = QtCore.QCoreApplication.translate
        SelectComponents.setWindowTitle(_translate("SelectComponents", "SelectComponents"))
        self.pushButton.setText(_translate("SelectComponents", "进入系统"))
        self.pushButton_2.setText(_translate("SelectComponents", "退出系统"))
        self.label.setText(_translate("SelectComponents", "选择元器件"))
 
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    login = Ui_welcome()
    login.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())


