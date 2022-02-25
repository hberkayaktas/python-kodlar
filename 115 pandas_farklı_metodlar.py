import pandas as pd

nüfus = pd.read_csv("00extras/dünyanüfusu.csv")
print(nüfus)


#satırlarında NaN yani boş datalar olan satırları atma
print(nüfus.dropna(how="any"))

#satır değeri fark etmeksizin tüm tabloyu alma
print(nüfus.dropna(how="all"))

#boş satırları silme(yoksayma)
print(nüfus.dropna(subset=["Ortalama yaş"]))

#NaN değerleri 1 ile doldurma
print(nüfus.fillna(1))

#tek bir stunu çağırma
print(nüfus["Doğum oranı"])

#NaN ları doldurma ve üzerine kalıcı hale getirme
nüfus["Doğum oranı"].fillna(1,inplace=True)
print(nüfus)

#tablo bilgilerini alma
print(nüfus.info())

#belirli stunu oluşturma ve değer atama
nüfus["Sıralama"]= nüfus["Sıralama"].fillna(1.0)
print(nüfus)

#stun data tipini değiştirme
nüfus["Sıralama"]= nüfus["Sıralama"].astype("int")
print(nüfus)

#sıralama yapma
print(nüfus.sort_values("Ortalama yaş",ascending=False))

#kendi içinde iki farklı sıralama
print(nüfus.sort_values(["Ortalama yaş","Şehirleşme oranı"],ascending=[False,True]))

#indexe göre sıralama
print(nüfus.sort_index(ascending=False))

#tabloyu alırken editleme
nüfus = pd.read_csv("00extras/dünyanüfusu.csv").dropna(how="any")
print(nüfus)

#sıralama yapıp stuna atama
nüfus["Yaş Sıralama"] = nüfus["Ortalama yaş"].rank(ascending=False).astype("int")
print(nüfus)


