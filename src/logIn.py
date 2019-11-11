# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import options
import incorrect
import null
import re
import database

class logIn(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()


    def correct(self):
        self.data=database.database("database","User",2,["name","TEXT","password","TEXT"])
        # name=self.data.select("User","name",self.lineEdit.text().replace(" ", ""))
        # print(name)
        database.database.id=self.lineEdit.text().replace(" ", "")
        print(database.database.id)

        if (self.lineEdit.text() == "" or self.lineEdit_2.text() == ""):
            self.ui = null.null()


        if  self.data.idFound("User",2,["name",self.lineEdit.text().replace(" ", ""),"password",self.lineEdit_2.text().replace(" ", "")]) :
            print("enter1")
            self.ui = options.options()
            self.close()
            self.ui.show()
        else:
            self.ui = incorrect.incorrect()
            self.close()
            self.ui.show()




    def initUI(self):
        self.setWindowTitle("Log In")
        self.resize(354, 153)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.setFont(font)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 100, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.correct)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", " Enter Your Name :"))
        self.label_2.setText(_translate("Dialog", " Enter Password   :"))
        self.pushButton.setText(_translate("Dialog", "Log In"))
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = logIn()
    sys.exit(app.exec_())

