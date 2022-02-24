from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    izgara = QGridLayout()

    for i in range(1,6):
        for j in range(1,6):
            izgara.addWidget(QPushButton("Str:{} Stn:{}".format(i,j)),i,j)
    window.setLayout(izgara)

    window.setWindowTitle("PyQt5")
    window.show()
    sys.exit(app.exec())
"""
    izgara.addWidget(QPushButton("Button1"), 1, 1)
    izgara.addWidget(QPushButton("Button2"), 1, 2)
    izgara.addWidget(QPushButton("Button3"), 1, 3)
    izgara.addWidget(QPushButton("Button4"), 2, 1)
    izgara.addWidget(QPushButton("Button5"), 2, 2)
    izgara.addWidget(QPushButton("Button6"), 2, 3)
"""

    

if __name__ == "__main__":
     pencere()