import requests

from bs4 import BeautifulSoup
#pip install bs4


imdburl = "https://www.doviz.com/"

r =  requests.get(imdburl)

soup = BeautifulSoup(r.content,"html.parser") #gelen bütün veri bölünür

gelen_veri = soup.find_all("div",{"class":"market-data"}) 
#table komutu altında chart full-width içindeki tüm elemanlar

#print(gelen_veri[0].contents)
#print(len(gelen_veri[0].contents))

#elemantablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents)-1] #liste halinde sonunncu hariç seçilir

elemantablosu = gelen_veri[0].find_all("span") #satırlara bölünür ,{"class":"name","value"}

print(elemantablosu[2].text)



i=0
while i <= 19:
    print(i,"---------------------------------------------------------------------------")
    print(elemantablosu[i].text)
    print(elemantablosu[i+1].text)
    print(elemantablosu[i+2].text.strip(),"\n")
    i = i+3
    if i==19:
        break


#i= 0
"""
for film in elemantablosu:
    i += 1
    filmbasliklari = film.find_all("span",{"class":"name"}) #baslık stunu seçiliyor
    print(filmbasliklari)
    filmismi = filmbasliklari[0].text 
    filmismi = filmismi.replace("\n","")
    print(filmismi)
    print("---------------------------------------------------------------------------")
"""