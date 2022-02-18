# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#stringler
isim = "Berkay AKTAŞ"
print(isim)
print(isim[1]) #2 karakter
print(isim[0:5]) #1 6 yakadar

print('türkiye\'nin enbüyük merkezi') #kaçış dizisi
print('türkiye\'nin \n enbüyük merkezi\n') #altsatıra geçer
print('türkiye\'nin  en\tbüyük merkezi') #boşluk bırakır
print("berkay"* 3) #stringi 3 leçarpar
print("berkay".upper()) #stingi büyütme
print("BERKAY".lower()) #küçültme
print("berkay aktas \n".capitalize()) #sadece baş harfi büyütme
#unutma bunlar kalıcı değişiklik yapmaz
print(isim.count("e")) #kac tane e var sayar
print(isim.find("Berkay")) #kac tane berkay var sayar
print(isim.index("e")) #seciili harfin yerini bulur

yeni_isim = "     .Hakan TEK.     "
#print(yeni_isim)
print(yeni_isim.lstrip()) #soldan siler
print(yeni_isim.rstrip()) #sagdan siler
print(yeni_isim.strip()) #gereksiz bosluk siler
print(yeni_isim.replace("TEK","NUR")) #yer değistirir
#format donksiyonu
isim2 = "burhan"
soyisim2 = "altintop"
print("benim ismim {} soy ismim {}".format(isim2,soyisim2))



x="berkay"
y='aktas' #ikiside stringdir

print(x+y) #boşulksuz string toplar