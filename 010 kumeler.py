# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Kümeler - Sets")
sayilar = {1,2,3,4,5,5,5,6,8,9,11,31}
#kümelerde tekrar eden sayılar okunmaz
print("1",sayilar)


sayilar.add(100) #kümeye eleman ekleme
print("2",sayilar)
sayilar.discard(5) #kümeden eleman çıkarma
print("3",sayilar)
sayilar.remove(3) #kümeden eleman silme
print("4",sayilar)

yeni = {11,31,41,52,68,85}
sayilar.update(yeni) #küme toplama
print(sayilar)

a = {1,2,4,6}
b = {2,4,5,6,7}

print(a.difference(b)) 
#a dan b yi cıkarınca ne kalıyor
print(a.intersection(b))
#a ve be ortak küme grubu
print(a.union(b))
#a ve b birleşim kümesi
print(len(a))
#küme eleman sayısı