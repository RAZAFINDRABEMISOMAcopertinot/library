from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pymysql

from PyQt5.uic import loadUiType

ui, _ = loadUiType('library.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.Hide_Theme()

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Theme)
        self.pushButton_21.clicked.connect(self.Hide_Theme)

    def Show_Theme(self):
        self.groupBox_6.show()

    def Hide_Theme(self):
        self.groupBox_6.hide()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()