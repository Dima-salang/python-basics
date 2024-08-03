from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 200, 200, 200)
        self.setWindowTitle("Contacts")
        self.setGeometry(500, 200, 200, 200)
        self.setWindowTitle("Contacts")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.move(50, 50)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Click me!")
        self.button1.move(50, 70)
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("I transformed!")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
