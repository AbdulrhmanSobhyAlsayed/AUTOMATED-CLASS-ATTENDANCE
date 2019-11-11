# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doneui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class null(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def exit(self):
        self.close()
    def initUI(self):
        self.setWindowTitle("Null")
        self.resize(470, 119)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 0, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 60, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.exit)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Enter Your Name And The Password"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = null()
    sys.exit(app.exec_())

