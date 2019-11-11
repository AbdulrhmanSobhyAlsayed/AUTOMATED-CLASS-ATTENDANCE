from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import database
import re

import sys
import options

class wasDelete(QDialog):
    def __init__(self):
        super(wasDelete,self).__init__()
        loadUi('wasDelete.ui',self)
        self.pushButton.clicked.connect(self.exit)

    def exit(self):
        self.op=options.options()
        self.close()
        self.op.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = wasDelete()
    ex.show()
    sys.exit(app.exec_())