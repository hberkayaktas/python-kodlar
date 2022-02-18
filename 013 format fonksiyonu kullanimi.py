# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:07:06 2021

@author: hberk
"""

print("oyuncu kaydetme programı")
ad = input("Oyuncunun adı:")
soyad = input("Oyuncunun soyadı:")
takim = input("Oyuncunun takım adı:")

bilgiler =[ad,soyad,takim]

print("kaydediliyor")

#format kullanımı

print("oyuncunun adı:{}\nOyuncunun soyadı:{}\ntakımı:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

#süslü parantez olan yerlere format fonksiyonu indexe göre dolum yapar doldurur
print("kaydedildi")
