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
        self.media = QMediaPlayer()
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile("01 simge/arkaplan.mp3")))

        #QSlider
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setMinimum(0)
        self.s1.setMaximum(100)

        #QLabel
        self.yazim = QLabel("%")
        self.yuzdelikgosterge = QLabel()

        #BaslatButtonAyar
        self.baslatButton = QPushButton()
        self.baslatButton.setIcon(QIcon("01 simge/baslat.png"))

        #Durdur Button
        self.durdurButton = QPushButton()
        self.durdurButton.setIcon(QIcon("01 simge/durdur.png"))

        #VBOX
        v_box = QVBoxLayout()

        #HBOX 1
        h_box = QHBoxLayout()
        h_box.addWidget(self.yazim)
        h_box.addWidget(self.yuzdelikgosterge)

        #HBOX 2
        h_box2 = QHBoxLayout()
        h_box.addWidget(self.baslatButton)
        h_box.addWidget(self.durdurButton)

        #Duzenleme Box islemleri
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.s1)

        #Baslat Calisinca
        self.baslatButton.clicked.connect(self.cal)

        #Durdur Calısınca
        self.durdurButton.clicked.connect(self.durdur)

        #Slidera Bağlı yapı
        self.s1.valueChanged.connect(self.ses)

        self.setLayout(v_box)
        self.show()
        self.setWindowTitle("QSlider")

    def cal(self):
        self.media.play()
    def durdur(self):
        self.media.pause()
    def ses(self):
        self.yuzdelikgosterge.setText(str(self.s1.value()))
        self.media.setVolume(int(self.s1.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())