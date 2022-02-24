from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    button = QPushButton(window)
    button.setIcon(QIcon("01 simge/simge.png"))

    h_box = QHBoxLayout()
    h_box.addWidget(button)


    window.setLayout(h_box)
    window.setWindowTitle("PyQt5")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
     pencere()