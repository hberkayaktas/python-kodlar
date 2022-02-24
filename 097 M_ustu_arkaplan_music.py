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
        self.setGeometry(100,100,200,200)
        self.setAutoFillBackground(True)
        #self.showFullScreen()

        self.p = self.palette()
        self.p.setColor(self.backgroundRole(),Qt.black)

        self.setPalette(self.p)

        self.media = QMediaPlayer()
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile("01 simge/arkaplan.mp3")))

        self.sp = QSpinBox()
        self.sp.setRange(1,100)

        button = QPushButton("Şarkıyı çal")
        button2 = QPushButton("Çıkış")
        v_box = QVBoxLayout()
        v_box.addWidget(button)
        v_box.addWidget(self.sp)
        v_box.addWidget(button2)

        button2.clicked.connect(self.close)

        self.sp.valueChanged.connect(self.sesDegistir)
        button.clicked.connect(self.sarkiBaslat)


        self.setLayout(v_box)
        self.show()
        self.setWindowTitle("medya")


    def sesDegistir(self):
        self.media.setVolume(self.sp.text())
    def sarkiBaslat(self):
        self.sp.setValue(10)
        self.media.play()
        print("sarki oynatılıyor")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())