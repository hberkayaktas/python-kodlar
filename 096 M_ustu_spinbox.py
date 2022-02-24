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
        self.sp = QSpinBox() #spin box tanımlandı
        v_box = QVBoxLayout()

        self.sp.setRange(100,1000) #aralık bu şekilde tanımlana biliyor 100-200
        self.sp.setValue(300)  # varsayılan değer olarak 300tanımladık
        self.sp.valueChanged.connect(self.uygula)
        #self.sp.setMinimum(200)     #spin box un minimum değeri
        #self.sp.setMaximum(1000)    #spin box un maximum değeri
        #self.sp.setSingleStep(5)    #spin box un 5 er 5 er artması

        self.sp2 = QDoubleSpinBox()
        self.sp2.setRange(120, 220)
        self.sp2.setValue(150)
        self.sp2.setSingleStep(0.1)
        self.sp2.valueChanged.connect(self.uygula2)

        v_box.addWidget(self.sp)
        v_box.addWidget(self.sp2)

        self.setLayout(v_box)
        self.show()
        self.setWindowTitle("Spin Box")
    def uygula(self):
        print("şuanki değer :{}".format(str(self.sp.value())))
    def uygula2(self):
        print("Boyunuz :{}".format(str(self.sp2.value())))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())