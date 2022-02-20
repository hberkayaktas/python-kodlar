# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 03:17:02 2022

@author: hberk
pip install qrcode pillow
"""

import qrcode

code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 100, #boyut
    border = 4 #kenar kalınlığı
)

code.add_data("https://www.youtube.com/watch?v=I8mY-jDO8Lc")
code.make(fit=True)

image= code.make_image(fill_color=(8,153,206),back_color ="white")
image.save("00 extras/qrcode2.png")