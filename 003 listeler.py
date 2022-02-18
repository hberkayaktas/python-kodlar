# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Listeler")
calisan = ["0hakan","1uzum",29,'3writer']
print(calisan)
print(calisan[3])
#degistirmeyapma
calisan[1] = "günaydin"
print(calisan)
#liste içi liste ekleme
insanlar =[["nuri","yilmaz",29],["eylül","atsiz"]]
print(insanlar)
print(insanlar[0])
print(insanlar[1])
#misal "eylül" ismine ulasalim
print(insanlar[1][0])
#kac eleman var listede
print(len(insanlar))
#ilk indexte ne tanimli
print(len(insanlar[0]))

#listeye birseyler ekleme 
insanlar[0].append("yazilimci")
print(insanlar[0])

insanlar[0] = insanlar[0] + ["yazilimci"] #veya bu yöntem

#listeden birseyler cikarma
insanlar[0].remove(29) #veya "yazilimci"
print(insanlar[0])
#indexli silme
insanlar[0].pop(2) #ikinci index yazilimci silindi
print(insanlar[0])

#iki listeyi birleştirme
a = ["nuri",5]
b = ["yilmaz",29]
c = a + b
print(c)
#metotla birlestirme
birinci = [1,2,3,4]
ikinci = [6,7,8,9,10]
birinci.extend(ikinci)
print(birinci)
#sayici
ucuncu = [6,7,8,7,9,7,10]
print("sayici",ucuncu.count(7))
#index bulucu
print("index",ucuncu.index(9))
print("index2",ucuncu.index(7))
#kaçtane geçtiği fark etmeksizin ilk buldugunun yerini yazar

#indexli ekleme
ucuncu.insert(5,"yazdir")
print("eklenen hali",ucuncu)

#sıralama yapma
li = [5,4,8,1,6,3,7,2,9]
li.sort()
print(li) 
#ters siralama
li.sort(reverse = True)
print(li)
#alfabetik olarak da oluyor
isimler =["cemil","ahmet","baris"]
isimler.sort()
print(isimler) 
#ters siralama
isimler.sort(reverse = True)
print(isimler)

#liste bosaltma
isimler.clear()
print(isimler)