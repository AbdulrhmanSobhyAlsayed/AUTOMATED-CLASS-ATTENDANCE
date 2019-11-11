# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'incorrect.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import sys
import mainWindow



class incorrect(QDialog):
    def __init__(self):
        super(incorrect,self).__init__()
        loadUi('incorrect.ui',self)
        self.setWindowTitle("Incorrect")
        self.pushButton.clicked.connect(self.ok)


    def ok(self):
        self.ui = mainWindow.mainWindow()
        self.close()
        self.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = incorrect()
    ex.show()
    sys.exit(app.exec_())

