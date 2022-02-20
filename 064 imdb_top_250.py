import requests
import urllib.request
from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top"

r =  requests.get(imdburl)

soup = BeautifulSoup(r.content,"html.parser")

gelen_veri = soup.find_all("table",{"class":"chart full-width"})

#print(gelen_veri[0].contents)
#print(len(gelen_veri[0].contents))

filmtablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]

filmtablosu = filmtablosu.find_all("tr")
i= 0
for film in filmtablosu:
    i += 1
    filmbasliklari = film.find_all("td",{"class":"titleColumn"})
    filmismi = filmbasliklari[0].text
    filmismi = filmismi.replace("\n","")
    print(filmismi)
    print("---------------------------------------------------------------------------")



import urllib.request


url1 ="https://www.iconsdb.com/icons/preview/white/whatsapp-xl.png"
url2 ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9FERS8UUHMor64KSyXdMPj63ZUsVkgyuINBpqM5OVkWl_C75i"
url3 ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVFA5QShn-47G2LQbuUrg33ldpgrEObpR8iNwHFQx8hSxoxFg6"

urllistesi =[url1,url2,url3]

say = 1

for url in urllistesi:
    urllib.request.urlretrieve(url,"Resim" + str(say)+".jpg")
    say +=1