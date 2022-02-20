import requests
from bs4 import BeautifulSoup


headers_param = {""}
web_link = requests.get("")

site_icerik = web_link.content

soup = BeatifulSoup(site_icerik,"html.parser")

all_site_icerik = soup.find_all("p",{"class":"class iceriği"})



for tekli_icerik in all_site_icerik:
	print(tekli_icerik.a.text)
	
tum_veri = soup.find_all("div",{"class","class iceriği"})
for data in tum_veri:
	print(data.text)