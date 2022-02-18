# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:46:44 2021

@author: hberk
"""

defkullannici ="yazilimci"
defparola ="1234"

kullanici=input("kullanıcı adı:")
parola=input("parolanız:")

if((defkullannici == kullanici) and (defparola == parola)):
    print("yazilim bilimi sitesine hoş geldiniz")
elif((defkullannici != kullanici) and (defparola == parola)):
    print("kullanıcı adı yanlış")
elif((defkullannici == kullanici) and (defparola != parola)):
    print("parola yanlış")
else :
    print("tekrar deneyin")