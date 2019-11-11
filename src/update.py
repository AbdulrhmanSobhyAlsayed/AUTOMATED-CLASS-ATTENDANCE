from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from PyQt5.uic import loadUi
import options
import studentUsed
import logIn
import sys
import database
import re
class update(QDialog):
    def __init__(self):
        super(update,self).__init__()
        loadUi('update.ui',self)
        self.setWindowTitle("Update")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = update()
    ex.show()
    sys.exit(app.exec_())