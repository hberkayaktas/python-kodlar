from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
    def yap():
        giris.setText("")

    app = QApplication(sys.argv)
    window = QWidget()

    giris = QLineEdit() #İnput box tanımladık
    giris2 = QTextEdit() #Text box tanımladık

    #giris.setReadOnly(True)  input boxu kitleme

    giris.setText("Mert Mekatronik") # box un içine yazı yazdırmak
    #giris.textChanged.connect(yap) giris input una tıklayınca yap fonksiyonunu calıştır
    

    #giris.setEchoMode(QLineEdit.Password) #input boxu password boxa çevirdik

    #giris.setInputMask("+999_999_99_99") # belli bir şablon tanımladık

    v_box = QVBoxLayout()
    v_box.addWidget(giris)
    v_box.addWidget(giris2)


    window.setLayout(v_box)

    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
     pencere()