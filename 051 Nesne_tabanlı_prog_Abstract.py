print("Nesne tabanlı Programlama 3")

#3.Abstract Class ( Soyut Sınıflar)
#Soyut sınıflar aslında var olmayan şablon nesnelerdir 
#yeni nesne üretiminde kullanılır
#Bu soyut sınıflar alt sınıflar için
#  bir şablon görevi görürler. 
# Soyut sınıfların İki tane özelliği var.


#soyut sınıftan nesne üretilemez

from abc import ABC,abstractmethod

class Hayvan(ABC):
    @abstractmethod
    def yürü(self):
        pass

    @abstractmethod
    def koş(self):
        pass

#Alt sınıfta bu metodları 
#kullanacaksanız orada yeniden tanımlanmalı

class kedi(Hayvan):
    def yürü(self):
        print("kedi yürüyor")
    def koş(self):
        print("kedi koşuyor")

#kuş = Hayvan()
#soyut sınıftan bir nesne üretilmez yukarıdaki kod hata verir

bir = kedi()
bir.yürü()
