from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import options
import re

import sys

class deleted(QDialog):
    def __init__(self):
        super(deleted,self).__init__()
        loadUi('deleted.ui',self)
        self.setWindowTitle("Delete")
        self.pushButton.clicked.connect(self.exit)

    def exit(self):
        self.op=options.options()
        self.close()
        self.op.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = deleted()
    ex.show()
    sys.exit(app.exec_())