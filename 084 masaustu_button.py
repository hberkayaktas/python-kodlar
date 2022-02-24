from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    v_box = QVBoxLayout()

    button1 = QPushButton("kabul ediyotum")

    button2 = QPushButton("red ediyorum")

    v_box.addWidget(button1)
    v_box.addStretch()
    v_box.addWidget(button2)

    window.setLayout(v_box)


    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
     pencere()