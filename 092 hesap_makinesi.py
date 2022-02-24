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
        form = QFormLayout()

        self.giris1 = QLineEdit()
        self.giris2 = QLineEdit()
        gonder = QPushButton("Hesapla !")
        self.yazi1 = QLabel("Sayi 1 :")
        self.yazi1.setFont(QFont("Helvetica",14,QFont.Bold))
        self.sonuc = QLabel()
        self.sonuc.setAlignment(Qt.AlignCenter)
        self.yazi2 = QLabel("Sayi 2 :")
        self.yazi2.setFont(QFont("Helvetica",14,QFont.Bold))



        self.r1 = QRadioButton("Topla")
        self.r2 = QRadioButton("Çıkar")
        self.r3 = QRadioButton("Çarp")
        self.r4 = QRadioButton("Böl")

        form.addRow(self.yazi1,self.giris1)
        form.addRow(self.yazi2,self.giris2)




        h_box3 = QHBoxLayout()


        h_box3.addWidget(self.r1)
        h_box3.addWidget(self.r2)
        h_box3.addWidget(self.r3)
        h_box3.addWidget(self.r4)

        form.addRow(h_box3)
        form.addRow(self.sonuc)
        form.addRow(gonder)

        gonder.clicked.connect(self.hesapla)

        self.setLayout(form)
        self.show()
        self.setWindowTitle("İlkel Hesap makinesi")

    def hesapla(self):
        if self.r1.isChecked():
            sayi1 = float(self.giris1.text())
            sayi2 = float(self.giris2.text())
            toplam = sayi1 + sayi2
            toplam = str(toplam)
            self.sonuc.setText(toplam)
        elif self.r2.isChecked():
            sayi1 = float(self.giris1.text())
            sayi2 = float(self.giris2.text())
            toplam = abs(sayi1 - sayi2)
            toplam = str(toplam)
            self.sonuc.setText(toplam)
        elif self.r3.isChecked():
            sayi1 = float(self.giris1.text())
            sayi2 = float(self.giris2.text())
            toplam = sayi1 * sayi2
            toplam = str(toplam)
            self.sonuc.setText(toplam)
        elif self.r4.isChecked():
            sayi1 = float(self.giris1.text())
            sayi2 = float(self.giris2.text())
            toplam = sayi1 / sayi2
            toplam = str(toplam)
            self.sonuc.setText(toplam)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())