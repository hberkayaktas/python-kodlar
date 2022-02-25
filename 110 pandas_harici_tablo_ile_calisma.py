import pandas as pd

#tabloyu okuma
ülke = pd.read_csv("00extras/ülke.csv")
#harici olarak alırız üzerinde işlem yapılabilir biçim değil
#salt okunur haldedir
print(ülke)

#sıkıştırılmış tablo halinde okuma ileriki versiyonlarda kaldırılacak
ülke2 = pd.read_csv("00extras/ülke.csv",squeeze=True)
print(ülke2)

#harici tablo tekrar
gelir = pd.read_csv("00extras/milligelir.csv")

#önce bir tabloyu okutalım
print(gelir)

#ilk 5 veri
print(gelir.head(5))

#son 5 rakam
print(gelir.tail(5))

