from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    h_box = QHBoxLayout()

    button1 = QPushButton("kabul ediyotum")
    button2 = QPushButton("red ediyorum")
    button3 = QPushButton("2")
    button4 = QPushButton("3")

    v_box = QVBoxLayout()
    h_box = QHBoxLayout()


    v_box.addWidget(button1)    #uzaya bilen tuş
    v_box.addStretch()          #iki buton arasındaki sonsuz uzunluk
    v_box.addWidget(button2)

    h_box.addWidget(button3)
    h_box.addStretch()
    h_box.addWidget(button4)

    v_box.addLayout(h_box)


    window.setLayout(v_box)
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
     pencere()