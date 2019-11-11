# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
import signUp
import logIn
import sys
import database


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.database()
        self.initUI()

    def login(self):
        self.ui = logIn.logIn()
        self.close()
        self.ui.show()

    def signUpWindow(self):
        self.ui1 = signUp.signUp()
        self.close()
        self.ui1.show()

    def exitWindow(self):
        self.close()

    def database(self):
        self.data=database.database("database","User",2,["name","TEXT","password","TEXT"])


    def initUI(self):
        self.setWindowTitle("Class Attendance")
        self.resize(292, 289)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.setFont(font)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.signUpButton = QtWidgets.QPushButton(self)
        self.signUpButton.setGeometry(QtCore.QRect(80, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signUpButton.setFont(font)
        self.signUpButton.setObjectName("signUpButton")
        self.signUpButton.clicked.connect(self.signUpWindow)
        self.logInButton = QtWidgets.QPushButton(self)
        self.logInButton .setGeometry(QtCore.QRect(80, 140, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logInButton .setFont(font)
        self.logInButton .setObjectName("logInButton ")
        self.logInButton.clicked.connect(self.login)
        self.exit = QtWidgets.QPushButton(self)
        self.exit.setGeometry(QtCore.QRect(80, 200, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.exitWindow)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#aa0000;\">CLASS ATTENDANCE </span></p></body></html>"))
        self.signUpButton.setText(_translate("Dialog", "Sign Up"))
        self.logInButton .setText(_translate("Dialog", "Log In"))
        self.exit.setText(_translate("Dialog", "Exit"))
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())
