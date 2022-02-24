from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from bs4 import BeautifulSoup

import sys
import requests

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.cb = QCheckBox("Anlaşmayı Okudum onaylıyoum")
        button = QPushButton("Gönder")

        h_box = QHBoxLayout()
        h_box.addWidget(self.cb)
        h_box.addWidget(button)


        button.clicked.connect(self.yap)
        self.setLayout(h_box)
        self.show()
        self.setWindowTitle("CheckBox")

    def yap(self):
        if self.cb.isChecked():
            print("anlasma kabul edilmiş")
        else:
            print("anlaşma kabul edilmemiş")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())