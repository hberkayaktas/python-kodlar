import pandas as pd

ülke = pd.read_csv("00extras/dünya.csv")
print(ülke)

#ilk 5 satırı alma
c = ülke.head()
print(c)

#son 3 satırı alma
g = ülke.tail(3)
print(g)

#index sayısını öğrenme
f = ülke.index
print(f)

#data frame boyutlarını öğrenme
p = ülke.shape
print(p)

#stunları öğrenme
l = ülke.columns

#df nin eksenlerini öğrenme
o = ülke.axes
print(o)

#df nin tüm tanımlamaları
r = ülke.info()
print(r)
