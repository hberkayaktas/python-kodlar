from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


def pencere():
   

    app = QApplication(sys.argv)
    window = QWidget()
    form = QFormLayout()

    #pencere ana iskeleti 



    window.setLayout(form)
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
     pencere()