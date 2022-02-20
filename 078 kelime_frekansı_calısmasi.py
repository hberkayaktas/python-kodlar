import requests
import operator

from bs4 import BeautifulSoup

"""
bu proje belirli bir internet 
sitesinde geçen kelimelerin 
sayısını bulur ve listeler
"""


def sozlukolustur(tumkelimeler):
    kelimesayisi ={}
    for kelime in tumkelimeler:
        if kelime in kelimesayisi:
            kelimesayisi[kelime] +=1
        else:
            kelimesayisi[kelime] =1
    return kelimesayisi



def sembolleritemizle(tumkelimeler):
    sembolsuzkelimeler = []
    semboller ="!@$#^*()%+_{}\"<>?,.:“”/’'[]-=—1234567890" + chr(775)
    for kelime in tumkelimeler :
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")
        if (len(kelime) > 0):
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler



url = "https://www.wikizero.com/tr/Mustafa_Kemal_Atat%C3%BCrk"

tumkelimeler = []

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")



for kelimegruplari in soup.find_all("p"):
    icerik = kelimegruplari.text
    kelimeler = icerik.lower().split()


    for kelime in kelimeler:
        tumkelimeler.append(kelime)
       # print(kelime)

tumkelimeler = sembolleritemizle(tumkelimeler)
kelimesayisi = sozlukolustur(tumkelimeler)

for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)): #alfabeye göre dizmek için itemgetter 0 olamalı
   print(anahtar,"----->",deger)