#comment first
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
        app =  QApplication(sys.argv)
        win =  QMainWindow()
        win.setGeometry(1200, 300, 500, 500)
        win.setWindowTitle("From CDP")
        win.setWindowIcon(QIcon("ars.png"))
        win.setToolTip("App DEV")


        lbl_name = QtWidgets.QLabel(win)
        lbl_name.setText('Enter Your Name: ')
        lbl_name.move(20,20)

        lbl_name = QtWidgets.QLabel(win)
        lbl_name.setText('Enter Your password: ')
        lbl_name.move(20,50)

        txt_name = QtWidgets.QLineEdit(win)
        txt_name.move(200,50)

        
        txt_pw = QtWidgets.QLineEdit(win)
        txt_pw.move(200,90)   
        def clicked(self):
            print('button clicked')
            print('name :' + txt_name.text())
            print('password ' + txt_pw.text())

        btn_save = QtWidgets.QPushButton(win)
        btn_save.setText('Save')
        btn_save.clicked.connect(clicked)
        btn_save.move(200, 130)
        
        win.show()
        sys.exit(app.exec_())


window()
