from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
    app = QApplication(sys.argv)
    window = QWidget()
    form = QFormLayout()
    def cikis():
        sys.exit(app.exec())

    label = QLabel("merhaba ben giriş sistemi")
    label.setAlignment(Qt.AlignCenter) #AlignCenter orta, AlignRight sağ
    label.setFont(QFont("Helvetica",20,QFont.Bold)) # yazı tipi falan

    label2 = QLabel()
    label2.setText("<a href=\"www.google.com\" >Gooogle </a>")
    label2.setAlignment(Qt.AlignCenter)
    label2.setOpenExternalLinks(True)

    label3 = QLabel()
    label3.setPixmap(QPixmap("Resim3.jpg"))




    form.addRow(label)
    form.addRow(label2)
    form.addRow(label3)
    form.addRow(QLabel("Kullanıcı Adı:"),QLineEdit())
    sifre = QLineEdit()
    sifre.setEchoMode(QLineEdit.Password)
    form.addRow(QLabel("şifre :"),sifre)
    form.addRow(QLabel("Adress : "),QTextEdit())

    h_box = QHBoxLayout()
    r1 = QRadioButton("Erkek")
    r2 = QRadioButton("Kadın")
    h_box.addWidget(r1)
    h_box.addWidget(r2)

    form.addRow(QLabel("Cinsiyet :"),h_box)

    h_box2 = QHBoxLayout()
    v_box = QVBoxLayout()
    v_box.addStretch()
    form.addRow(v_box)

    btn1 = QPushButton("Gönder")
    btn2 = QPushButton("iptal")
    btn2.clicked.connect(cikis)
    h_box2.addWidget(btn1)
    h_box2.addWidget(btn2)

    form.addRow(h_box2)

    window.setLayout(form)
    window.setWindowTitle("PyQt5")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
     pencere()