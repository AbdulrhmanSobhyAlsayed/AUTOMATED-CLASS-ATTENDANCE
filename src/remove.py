from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import database
import re
import  wasDelete
import deleted
import sys

class remove(QDialog):
    def __init__(self):
        super(remove,self).__init__()
        loadUi('remove.ui',self)
        self.setWindowTitle("Remove")
        self.removeButton.clicked.connect(self.remove)

    def remove(self):
        id = database.database.id
        print(id)
        self.data=database.database("database","StudentInfo",3,["id","TEXT","name","TEXT","image","TEXT"])
        # x = (self.data.select("StudentInfo", "name", self.studentName.text()))
        # print(x)
        # if(len(x)==0):
        #     self.wa=wasDelete.wasDelete()
        #     self.close()
        #     self.wa.show()

        if self.data.idFound("StudentInfo",2,["id",id,"name",self.studentName.text()]):
            print(self.data.selectAll("StudentInfo"))
            self.data.deletRow("StudentInfo","name",self.studentName.text())
            print(self.data.selectAll("StudentInfo"))
            self.de=deleted.deleted()
            self.close()
            self.de.show()
        else:
            self.wa=wasDelete.wasDelete()
            self.close()
            self.wa.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = remove()
    ex.show()
    sys.exit(app.exec_())