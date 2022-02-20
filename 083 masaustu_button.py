from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
    app = QApplication(sys.argv)
    pencere = QDialog()
    pencere.setGeometry(100, 100, 300, 300)
    ####################### pencere boyutu tanımlandı #############################
    button1 = QPushButton(pencere)
    button1.setText("Tıklama Alanı 1")
    button1.move(20,30)
    button1.clicked.connect(button1Tiklandi)

    button2 = QPushButton(pencere)
    button2.setText("Tıklama Alanı 2")
    button2.move(20,100)
    button2.clicked.connect(button2Tiklandi)
    ####################### butonlar tanımlandı ############################

    pencere.show()
    sys.exit(app.exec())

def button1Tiklandi():
    print("button 1 e tiklandi")

def button2Tiklandi():
    print("button 2 ye tiklandi")

if __name__ == "__main__":
     pencere()