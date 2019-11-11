from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from PyQt5.uic import loadUi
import options
import studentUsed
import logIn
import sys
import database
import re
class addStudent(QDialog):
    def __init__(self):
        super(addStudent,self).__init__()
        loadUi('addStudent.ui',self)
        self.setWindowTitle("Add Student")
        self.path=""
        self.browse.clicked.connect(self.fileBrowsing)
        self.add.clicked.connect(self.insert)
        self.finish.clicked.connect(self.options)


    def options (self):
        self.ui = options.options()
        self.close()
        self.ui.show()


    def insert(self):
        print("enter")
        self.data=database.database("database","StudentInfo",3,["id","TEXT","name","TEXT","image","TEXT"])

        id=database.database.id
        print(id+"j")
        print(id)
        # x=(self.data.select("StudentInfo", "name", self.studentName.text()))
        # print(x)
        # if(len(x)==0):
        #     print("enter")
        #     self.data.insertRow("StudentInfo",3,["id",id,"name",self.studentName.text(),"image",self.studentImage.text()])

        if self.data.idFound("StudentInfo",2,["id",id,"name",self.studentName.text()]):
            self.no = studentUsed.studentUsed()
            self.close()
            self.no.show()
        else:
            print("enter")
            self.data.insertRow("StudentInfo",3,["id",id,"name",self.studentName.text(),"image",self.studentImage.text()])
        self.studentName.clear()
        self.studentImage.clear()

    def fileBrowsing(self):
        name = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.png)")
        self.path=name[0]
        print(self.path)
        self.studentImage.setText(self.path)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = addStudent()
    ex.show()
    sys.exit(app.exec_())

















