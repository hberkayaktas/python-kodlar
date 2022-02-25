from operator import ge
import pandas as pd

#veriyi çağıralım
ülke2 = pd.read_csv("00extras/ülke.csv",squeeze=True)
gelir = pd.read_csv("00extras/milligelir.csv",squeeze=True)
print(ülke2)
print(gelir)


print("Gömülü Fonksiyonlar")

#datanın satır uzunluğunu öğrenme
print(len(gelir))

#data tipini öğrenme
print(type(ülke2))

#sıralama yapma
print(sorted(ülke2))

#listeye atama
print(list(ülke2))

#sözlüğe atama yapma
print(dict(gelir))

#verideki enfazlayı bulma
print(max(gelir))

#verideki minimumu bulma
print(min(gelir))

#medyan
print(gelir.median())

#standart sapma
print(gelir.std())

#ortalama
print(gelir.mean())

#bu bilgileri ve dataframe özeti 
print(gelir.describe())



#ilk beş veriyi listeleme
print(ülke2.sort_values().head())

#geliri sıralama
print(gelir.sort_values()) #küçükten büyüğe
print(gelir.sort_values(ascending=False)) #büyükten küçüğe

g = gelir.sort_values(ascending=True,inplace=True) 
#inplace ile  kalıcı olur
print(g)

#dahil mi sorgulama
print("ABD" in ülke2.values) #abd ülke2 içinde varmı
#varsa true yoksa false

#index ile çağırma
print(ülke2[5])

print(ülke2[5:10])




