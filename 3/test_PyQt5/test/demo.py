import sys
from PyQt5 import QtWidgets,QtCore
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(400,100)
widget.setWindowTitle("this is a demo")
widget.show()

exit(app.exec_())
