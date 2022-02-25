import pandas as pd

yıllar = [2015,2016,2017,2018,2019]
gelir = [1000,2000,3000,4000,5000]

#iki datayı merge (birleştirme)
z = pd.Series(data = gelir , index=yıllar)
#indexi yıllar olarak tanımlar veriyi gelir olarak ekler
print(z)

sayı = [1,2,4,6,8,3,35]
sayı = pd.Series(sayı)
#ilk önce sayı yazılır
print(sayı)

#tüm sayılar toplamı
print(sayı.sum())

#serinin maximumu
print(sayı.max())

#serinin minimumu
print(sayı.min())

#
print(sayı.product())

#ortalama
print(sayı.mean())
