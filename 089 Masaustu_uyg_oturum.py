from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
    def yap():
        kadi = "Berkay"
        sifre = 123456

        if kadi == g1.text() and sifre == g2.text():
            durumLabel.setText("Hoş geldiniz !")
        else:
            durumLabel.setText("Kullanıcı adı veya şifre hatalı")
            g1.clear()
            g2.clear()

    app = QApplication(sys.argv)
    window = QWidget()
    form = QFormLayout()

    g1 = QLineEdit()
    g1.setFont(QFont("Helvetica",13))
    g2 = QLineEdit()

    button = QPushButton("Giriş Yap")
    durumLabel = QLabel("")
    durumLabel.setFont(QFont("Helvetica",13))

    g2.setEchoMode(QLineEdit.Password)

    kullaniciAdi = QLabel("Kullanıcı Adı : ")
    form.addRow(kullaniciAdi,g1)
    form.addRow(QLabel("Şifre : "),g2)
    form.addRow(button)
    form.addRow(durumLabel)

    button.clicked.connect(yap)



    window.setLayout(form)
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
     pencere()