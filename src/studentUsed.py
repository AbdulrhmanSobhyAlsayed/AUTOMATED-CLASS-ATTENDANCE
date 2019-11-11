# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'incorrect.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import addStudent



class studentUsed(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def ok(self):
        self.ui = addStudent.addStudent()
        self.close()
        self.ui.show()

    def initUI(self):
        self.setWindowTitle("Student used")
        self.resize(400, 121)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.ok)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "This name already exists !!.try again"))
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = studentUsed()
    sys.exit(app.exec_())

