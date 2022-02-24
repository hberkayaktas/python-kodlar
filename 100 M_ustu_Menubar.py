from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *

import sys

class Pencere(QMainWindow):         #değiştirdik *************************
    def __init__(self):
        super().__init__()
        self.widget = Widgetim()
        self.setCentralWidget(self.widget)
        self.setUI()

    def setUI(self):
        menu = self.menuBar()
        dosya = menu.addMenu("Dosya") #dosya isimli bar ekledim
        duzen = menu.addMenu("Duzenle")


        #String objesi
        yeniDosya = QAction("yeni dosya", self)
        yeniDosya.setShortcut("Ctrl + o")
        yeniDosya.setIcon(QIcon("open.png"))
        dosya.addAction(yeniDosya)

        #QAction ifadesi
        yazdir = QAction("Yazdir", self)
        yazdir.setShortcut("Ctrl + P")
        yazdir.setIcon(QIcon("print.png"))
        dosya.addAction(yazdir)

        #ayarlar barı  dosya>ayarlar>görüntü ayarları
        ayarlar = dosya.addMenu("Ayarlar")
        ayarlar.addAction("Ses Ayarları")
        ayarlar.addAction("Görüntü Ayarları")

        temizle = QAction("Temizle",self)
        temizle.setShortcut("Ctrl + J")
        duzen.addAction(temizle)

        dosya.triggered[QAction].connect(self.uygula)

        self.setWindowIcon(QIcon("baslat.png"))
        self.setWindowTitle("Menu barlı uygulama")
        self.show()

    def uygula(self,q):
        print(q.text())

class Widgetim(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        form = QFormLayout()
        form.addRow("İsminiz : ",QLineEdit())
        form.addRow("Soyadınız : ", QLineEdit())
        form.addRow("Yaşınız ", QSpinBox())
        form.addRow(QPushButton("Gönder"))
        self.setLayout(form)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())