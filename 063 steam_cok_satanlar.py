import requests
from bs4 import BeautifulSoup

imdburl = "https://store.steampowered.com/?l=turkish"

r =  requests.get(imdburl)

soup = BeautifulSoup(r.content,"html.parser") #gelen bütün veri bölünür

gelen_veri = soup.find_all("div",{"id":"tab_topsellers_content"}) 
#table komutu altında chart full-width içindeki tüm elemanlar

#print(gelen_veri[0].contents)
#print(len(gelen_veri[0].contents))

#elemantablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents)-1] #liste halinde sonunncu hariç seçilir

#elemantablosu = gelen_veri.find_all("a") #satırlara bölünür ,{"class":"name","value"}


elemantablosu_oyunisim = gelen_veri[0].find_all("div",{"class":"tab_item_name"})
elemantablosu_oyunfiyat = gelen_veri[0].find_all("div",{"class":"discount_final_price"})
elemantablosu_oyuntur = gelen_veri[0].find_all("div",{"class":"tab_item_top_tags"})


print(len(elemantablosu_oyunisim)) #oyun sayısını öğrendik
i= len(elemantablosu_oyunisim)
s = 0
while s <= i: 
    print(elemantablosu_oyunisim[s].text)
    print(elemantablosu_oyunfiyat[s].text)
    print(elemantablosu_oyuntur[s].text,"\n")
    s  = s+1 
    if s == i:
        break

"""
i=0
while i <= 19:
    print(i,"---------------------------------------------------------------------------")
    print(elemantablosu[i].text)
    print(elemantablosu[i+1].text)
    print(elemantablosu[i+2].text.strip(),"\n")
    i = i+3
    if i==19:
        break
"""

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