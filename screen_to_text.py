import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab
import numpy as np
import cv2
from PIL import Image

class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        self.path = ""
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin =event.pos() 
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        change = event.pos().x()-self.begin.x()
        self.end = QtCore.QPoint(self.begin.x()+change, self.begin.y()+change)
        # print()
        # self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        # print(x1, y1, x2, y2)
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        imageProcess(img)

        img.save(self.path + r"\capture.jpg")
        # img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

        # cv2.imshow('Captured Image', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

def imageProcess(img):
    pass

def getPath():
    path = r"C:\Users\fabia\CLionProjects\TierList\assets"
    return path
    userInput = input("bitte den Path eingeben: ")
    if(userInput == ""):
        return path
    else:
        return userInput

def app(path):
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.path = path
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())

if __name__ == '__main__':
    app(getPath())