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
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Theme)
        self.pushButton_21.clicked.connect(self.Hide_Theme)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)


        self.pushButton_8.clicked.connect(self.Add_New_Book)

        self.pushButton_14.clicked.connect(self.Add_New_Category)

    def Show_Theme(self):
        self.groupBox_6.show()

    def Hide_Theme(self):
        self.groupBox_6.hide()

    #######################################################
    ############## Opening tabs ###########################

    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)


    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)


    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)


    #######################################################
    #################### Books ############################

    def Add_New_Book(self):

        self.db = pymysql.connect(host='localhost', user='root', password='', db='library')
        self.cur = self.db.cursor()

        ################# Get From Input #######################
        book_title = self.lineEdit_2.text()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.CurrentText()
        book_author = self.comboBox_4.CurrentText()
        book_publisher = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_4.text()

    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass

    def Delete_Books(self):
        pass



    #######################################################
    #################### Users ############################


    def Add_New_User(self):
        pass

    def Login(self):
        pass

    def Edit_Users(self):
        pass

    #######################################################
    #################### Settings #########################

    def Add_New_Category(self):

        self.db = pymysql.connect(host='localhost', user='root', password='', db='library')
        self.cur = self.db.cursor()

        ################# Get From Input #######################
        category_name = self.lineEdit_20.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
            ''', (category_name))

        self.db.commit()
        print('Category was created.')

    def Add_New_Author(self):

        self.db = pymysql.connect(host='localhost', user='root', password='', db='library')
        self.cur = self.db.cursor()

        ################# Get From Input #######################
        author_name = self.lineEdit_21.text()



    def Add_New_Publisher(self):

        self.db = pymysql.connect(host='localhost', user='root', password='', db='library')
        self.cur = self.db.cursor()

        ################# Get From Input #######################
        publisher_name = self.lineEdit_22.text()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()