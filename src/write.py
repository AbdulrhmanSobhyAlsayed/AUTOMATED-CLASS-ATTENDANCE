from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from PyQt5.uic import loadUi
import options
import xlsxwriter
import sys
import database
import numpy as np

class write(QDialog):
    def __init__(self):
        super(write,self).__init__()
        loadUi('write.ui',self)
        self.writeButton.clicked.connect(self.write)
        self.browseButton.clicked.connect(self.fileBrowsing)

    def write(self):
        id=database.database.id
        self.workbook = xlsxwriter.Workbook(self.filePath.text())
        self.worksheet = self.workbook.add_worksheet()
        self.data=database.database("database","attendance",4,["id","TEXT","name","TEXT","date","TEXT","state","INTEGER"])
        info=np.asarray(self.data.select("attendance",1,["id",id]))
        print(info)
        titels=["name","date","attendance"]
        row=0
        col=0
        for i in titels:
            self.worksheet.write(row,col,i)
            col+=1
        dataToWrite=[]

        for i in range(len(info)):
            dataToWrite.append(info[i,2:])
        dataToWrite=np.unique(dataToWrite,axis=0)
        print(dataToWrite)

        row = 1

        for i in range(len(dataToWrite)):
            for j in range(3):
                self.worksheet.write(row, j, dataToWrite[i][j])
            row += 1
        self.workbook.close()
        self.op=options.options()
        self.close()
        self.op.show()

    def fileBrowsing(self):
        name = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\')
        self.path=name[0]
        print(self.path)
        self.filePath.setText(self.path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = write()
    ex.show()
    sys.exit(app.exec_())