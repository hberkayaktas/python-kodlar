# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:19:31 2021

@author: hberk
"""
defkullanici ="yazilimci"
defparola ="1234"

while (True):
    kullanici = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if ((kullanici==defkullanici) and (defparola==parola)):
        print("hoşgeldin",kullanici)
        break
    elif ((kullanici != defkullanici) and (defparola == parola)):
        print("kullanıcı adını yanlış girdiniz")
    elif ((kullanici == defkullanici) and (defparola != parola)):
        print("şifreniz yanlış")
        print("şifrenizi değiştirmek ister misiniz?(E/H)")
        cevap =input()
        if(cevap=="E"):
            yeniparola = input("yeniparola:")
            print("lütfen bekleyin")
            defparola= yeniparola
            print("şifre başarıyla değiştirildi")

    else:
        print("tekrar deneyin")
