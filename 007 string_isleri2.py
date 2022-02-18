# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:36:01 2021

@author: hberk
"""

#printler
x="berkay"
y='aktas'

print(x) #içindeki değişkeni yazar
print(x[5]) #Yazı içindeki belirli index
print(x[1:4]) # 1 den 4 kadar
print(x[1:]) #1 den sona kadar 
len(x) #string uzunluğu
print(x+y) #berkayaktas şeklinde yazar
print(x,y) #berkay aktas şeklinde yazar


# "yazılım"+ 3 dersen veya virgül dersen eror verir
#yazman gereken

print("yazilim"+ str(3)) #rakamı stringe çevirir
#eğer bir stringi bir rakama çevirmek istiyorsak

print(int("8")+5) #int stringi rakama çevirir