from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        form = QFormLayout()

        button1 = QPushButton("En sevdiğiniz dil")
        button2 = QPushButton("İsminizi giriniz")
        button3 = QPushButton("Yasiniz giriniz")

        self.giris1 = QLineEdit()
        self.giris2 = QLineEdit()
        self.giris3 = QLineEdit()

        form.addRow(button1, self.giris1)
        form.addRow(button2, self.giris2)
        form.addRow(button3, self.giris3)

        button1.clicked.connect(self.dilAl)##dilAl fonksiyonnuna yolladık
        button1.clicked.connect(self.isimAl)  ##dilAl fonksiyonnuna yolladık
        button1.clicked.connect(self.yasAl)  ##dilAl fonksiyonnuna yolladık
        self.setLayout(form)
        self.setWindowTitle("QSlider")
        self.show()

    def dilAl(self):
        diller = ("C++","Java","Javascript","Python","Ruby","Visual Basic","PHP")
        secilen,tamam = QInputDialog.getItem(self,"Sevdiğiniz Dil","Sevdiğiniz dili seciniz :",diller,0,False)
        if tamam:
            self.giris1.setText(str(secilen))
        #dilAl fonksiyonu diyalog kutusuoluşturup değer döndurdü

    def isimAl(self):
        secilen,tamam = QInputDialog.getText(self,"İsminiz","İsminiz Giriniz :")
        if tamam:
            self.giris2.setText(str(secilen))

    def yasAl(self):
        secilen,tamam = QInputDialog.getInt(self,"Yaş girme Alanı","Yaşnız")
        if tamam:
            self.giris3.setText(str(secilen))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())