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
        self.cb = QComboBox()
        self.cb.addItem("1990")
        self.cb.addItem("ordu")
        self.cb.addItem("berkay aktas")

        self.cb2 = QComboBox()
        self.cb2.addItems(["1990","1222","berkay aktaş"])


        h_box = QHBoxLayout()
        h_box.addWidget(self.cb)
        h_box.addWidget(self.cb2)

        self.cb3 = QComboBox()
        self.cb3.addItems(self.dogumTarihiDondur())
        self.chbox = QCheckBox("Kabul  ediyorum")
        self.button = QPushButton("Gönder")

        h_box.addWidget(self.cb3)
        h_box.addWidget(self.chbox)
        h_box.addWidget(self.button)

        self.button.clicked.connect(self.uygula)




        self.setLayout(h_box)
        self.show()
        self.setWindowTitle("ComboBox")
    def uygula(self):
        suankiyil = 2018
        kullanicidogumtarihi = int(self.cb3.currentText())
        yas = suankiyil- kullanicidogumtarihi
        print("yasiniz {}".format(yas))
    def dogumTarihiDondur(self):
        liste = [str(x) for x in range(1940,2000)]
        return liste




if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())