from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from PyQt5.uic import loadUi
import numpy as np
import sys
import options
import database
import face_recognition
from PIL import Image, ImageDraw
from datetime import datetime

class take(QDialog):
    def __init__(self):
        super(take,self).__init__()
        loadUi('takeui.ui',self)
        self.browseButton.clicked.connect(self.fileBrowsing)
        self.takeButton.clicked.connect(self.takeAttendance)


    def fileBrowsing(self):
        name = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.png)")
        self.path=name[0]
        print(self.path)
        self.classImage.setText(self.path)

    def takeAttendance(self):
        id=database.database.id
        date=str(datetime.today().strftime('%Y-%m-%d'))
        testImage=self.classImage.text()
        self.data=database.database("database","attendance",4,["id","TEXT","name","TEXT","date","TEXT","state","INTEGER"])
        self.readData=database.database("database","StudentInfo",3,["id","TEXT","name","TEXT","image","TEXT"])
        students=np.asarray(self.readData.select("StudentInfo",1,["id",id]))
        print(students)
        studentsName = []
        studentsImages = []

        for i in range(len(students)):
            studentsName.append(students[i][2])
            studentsImages.append(students[i][3])

        loadImages = []
        encode = []
        attendName = []
        for i in range(len(studentsImages)):
            loadImages.append(face_recognition.load_image_file(str(studentsImages[i])))
            encode.append(face_recognition.face_encodings(loadImages[i])[0])

        unknown_image = face_recognition.load_image_file(testImage)

        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        pil_image = Image.fromarray(unknown_image)
        draw = ImageDraw.Draw(pil_image)

        unknown=False

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(encode, face_encoding)
            print(matches)
            name = "Unknown"
            face_distances = face_recognition.face_distance(encode, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = studentsName[best_match_index]
                self.data.insertRow("attendance", 4, ["id", id, "name", name, "date", date, "state", 1])
                print(self.data.selectAll("attendance"))
                attendName.append(name)
                print(name+"   d")
            # else:
            #     unknown=True
            #
            # if (not (unknown)):
            #     print(name + "done")
            #     self.data.insertRow("attendance", 4, ["id", id, "name", name, "date", date, "state", 1])
            #     print(self.data.selectAll("attendance"))
            #     attendName.append(name)

            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
            text_width, text_height = draw.textsize(str(name))
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left + 6, bottom - text_height - 5), str(name), fill=(255, 255, 255, 255))
        absentName = list(set(studentsName) ^ set(attendName))
        for i in absentName:
            self.data.insertRow("attendance", 4, ["id", id, "name", i, "date", date, "state", 0])

        print(self.data.selectAll("attendance"))

        del draw
        pil_image.show()
        self.d=options.options()
        self.close()
        self.d.show()










if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = take()
    ex.show()
    sys.exit(app.exec_())