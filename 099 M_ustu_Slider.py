from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.s1 = QSlider(Qt.Horizontal) #yatay slider () arasında birşey olamsaydı vertical
        #self.s1.setTickPosition(QSlider.TicksAbove) #üste tırnakları  koyuyor
        self.s1.setTickPosition(QSlider.TicksBelow) #aşağıya tırnak ekliyoruz
        label1 = QLabel("Değer :")
        self.label2 = QLabel()
        self.label2.setFont(QFont("Helvetica",25))
        h_box = QHBoxLayout()
        h_box.addWidget(label1)
        h_box.addWidget(self.label2)

        self.s1.setMinimum(0)       #minimum nokta
        self.s1.setMaximum(100)     #maximum nokta
        self.s1.setSingleStep(5)    #adım miktarı

        self.s1.valueChanged.connect(self.yaz)

        v_box = QVBoxLayout()

        v_box.addLayout(h_box)
        v_box.addWidget(self.s1)


        self.setLayout(v_box)
        self.show()
        self.setWindowTitle("QSlider")

    def yaz(self):
        self.label2.setText(str(self.s1.value()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())