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
        baslik = QLabel("")
        aciklamalabel = QLabel("<a href='#'>Link :</a>")
        logo = QLabel()
        self.giris = QLineEdit()
        gonder = QPushButton()
        self.alinanEntryler = QTextEdit()

        #Baslik
        baslik.setText("""
        <a><h1><font color =\"black\">İnci sözlük entry Alıcı</font></h1></a>
        """)
        baslik.setFont(QFont("Helvetica",15,QFont.Bold))
        baslik.setAlignment(Qt.AlignCenter)

        #logo
        logo.setPixmap(QPixmap("01simge/logo.png"))
        logo.setAlignment(Qt.AlignCenter)

        #Button
        gonder.setIcon(QIcon("01simge/gonder.png"))

        #hbox
        h_box = QHBoxLayout()
        h_box.addWidget(aciklamalabel)
        h_box.addWidget(self.giris)
        h_box.addWidget(gonder)

        #vbox
        v_box = QVBoxLayout()
        v_box.addWidget(baslik)
        v_box.addWidget(logo)
        v_box.addWidget(self.alinanEntryler)
        v_box.addLayout(h_box)

        gonder.clicked.connect(self.uygula)


        self.setLayout(v_box)
        self.show()
        self.setWindowTitle("İnci Sözlük Entry Alıcı v2.1")

    def uygula(self):
        print("uygula çalışıyor")
        url = str(self.giris.text())
        response = requests.get(url)
        content = response.content

        soup = BeautifulSoup(content,"html.parser")


        liste = list()
        for i in soup.find_all("div",attrs = {"class":"entry-text-wrap"}):
            print(i.text)
            liste.append(i.text)

        print(liste)

        toplamYazi =""
        for i in liste:
            toplamYazi = toplamYazi + i + "\n"

        self.alinanEntryler.setText(toplamYazi)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())