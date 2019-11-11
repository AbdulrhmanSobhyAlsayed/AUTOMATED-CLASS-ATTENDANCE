from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import addStudent
import sys
import remove
import take
import write

class options(QDialog):
    def __init__(self):
        super(options,self).__init__()
        loadUi('options.ui',self)
        self.setWindowTitle("Options")
        self.addStudentButton.clicked.connect(self.addStudentWindow)
        self.removeButton.clicked.connect(self.remove)
        self.exitButton.clicked.connect(self.exit)
        self.takeButton.clicked.connect(self.takeAttendance)
        self.writeButton.clicked.connect(self.write)



    def addStudentWindow (self):
        self.ui = addStudent.addStudent()
        self.close()
        self.ui.show()

    def remove(self):
        self.rem=remove.remove()
        self.close()
        self.rem.show()

    def exit(self):
        self.close()

    def takeAttendance(self):

        self.ta=take.take()
        self.close()
        self.ta.show()
    def write(self):
        self.wr=write.write()
        self.close()
        self.wr.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = options()
    ex.show()
    sys.exit(app.exec_())