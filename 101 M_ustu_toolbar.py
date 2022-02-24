from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *

import sys

class Pencere(QMainWindow):         #değiştirdik *************************
    def __init__(self):
        super().__init__()
        self.setCentralWidget(anaPencere())
        self.setUI()

    def setUI(self):
        toolbar = self.addToolBar("File")
        toolbar2 = self.addToolBar("Edit")


#########################toool bar 1 ##########################################
        new = QAction(QIcon("01 simge/open.png"),"open",self)
        toolbar.addAction(new)

        ruller = QAction(QIcon("01 simge/ruller.png"),"ruller",self)
        toolbar.addAction(ruller)

        _print = QAction(QIcon("01 simge/print.png"),"print",self)
        toolbar.addAction(_print)

        toolbar.setOrientation(Qt.Vertical) #toolbar1 i dik çağırıyoruz

        toolbar.actionTriggered.connect(self.uygula) #toolbarda herhangi birşeye tıklanınca fonkisyon çalışıyor


######################## tool bar 2 ##########################################
        info = QAction(QIcon("01 simge/erase.png"),"info",self)
        toolbar2.addAction(info)

        ara = QLineEdit()
        ara.setPlaceholderText("Ara....")

        gonder = QPushButton("gönder")
        toolbar2.addWidget(ara)
        toolbar2.addWidget(gonder)

        toolbar2.setMovable(False) #toolbar 2'nin gezinme özelliğini deaktif  ettik

        close = QAction(QIcon("spray"),"close",self)
        toolbar2.addAction(close)

        toolbar2.actionTriggered.connect(self.uygula2)  #toolbar2de herhangi birşeye tıklanınca fonkisyon çalışıyor
##############################################################################


        self.setWindowIcon(QIcon("baslat.png"))
        self.setWindowTitle("Player")
        self.show()

    def uygula(self,q):
        if q.text() == "open" :
            self.setCentralWidget(anaPencere())
    def uygula2(self,q):
        if q.text() == "info":
            self.setCentralWidget(Bilgi())
        else:
            self.close()

class anaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        form = QFormLayout()
        form.addRow("isminiz :",QLineEdit())
        form.addRow("soyadınız :", QLineEdit())
        form.addRow("Yaşınız :", QLineEdit())
        self.setLayout(form)

class Bilgi(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        v_box = QVBoxLayout()
        label = QLabel("Berkay Aktas")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Helvetica",22,QFont.Bold))

        label2 = QLabel("2018 herhakkı saklıdır")
        v_box.addWidget(label)
        v_box.addWidget(label2)

        self.setLayout(v_box)

def main():
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())


main()