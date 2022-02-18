print("Some Built-in Function")

#mutlak değer fonksiyonu
print(abs(-5.6))

#ikili sistemde sayıların değerini verir
print(bin(4))


#listeye numara indexi ekleme
renkler = ["sarı", "beyaz","yesil","siyah"]
x = enumerate(renkler)
print(list(x))
print(renkler)

#döngülü şekilde yazma
for index,renk in enumerate(renkler):
    print(index,renk)


#listedeki maximum sayıyı verir
x = [2,3,7,4,12,35]
print(max(x))

#bu fonksiyon alfabetik olarak da çalışır
y=["c","d","s","v","z","l"]
print(max(y))

#yine aynı şekilde listelerdeki en küçük ifadeyi veren fonk
print(min(y))
print(min(x))

#ters sıralama fonksiyonu
ters = reversed(x)
print(list(ters))
#yine alfabetik de çalışır


#kare alma fonksiyonu eğer
#ilk değer ,üssün n. kuvveti , ve kaç tabanında olduğu
#birşey yazılmaz ise 10 tabanında çalışır
print(pow(2,10)) #2 nin 10. kuvveti
print(pow(2,2)) #2 nin 2. kuvv
print(pow(5,2,10)) #5 in karesi


#yuvarlama fonksiyonu
z = round(3.14159265)
rnd = round(3.14159265,4) #virgülden sonra 4. basamak 
#tan sonrası yuvarlanır
print(z)
print(rnd)


#sıralama sorted() fonksyonu
i =[2,3,5,7,35,49]
print(sorted(i)) #düz sıralanmış
print(sorted(i,reverse=True)) #ters sıralanmış

#toplama fonksiyonu 
print(sum(i))

#iki listenin eşleştirilmesi
x =[1,2,3,4]
renkler=["sarı","siyah","beyaz","kırmızı"]
print(list(zip(x,renkler)))

