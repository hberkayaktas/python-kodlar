from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Merhaba Arayüz tasarımı")  # pencereye isim verme
    window.setGeometry(200, 200, 300, 300)  # arayüzün sınırlarını belirledik
    ###################################################################################

    yazi = QLabel(window) #Label kodu ile çağırdık
    yazi.setText("bu arayüzde bulunan bir yazıdır") #ara yüze yazı ekledik
    yazi.move(50,100)  #yaziyi taşıyoruz
    ###################################################################################

    alan = QLineEdit(window) #text box ekliyoruz
    alan.move(100,200)  #text box u taşıyoruz

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()