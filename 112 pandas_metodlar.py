from msilib.schema import tables
import pandas as pd

milli = pd.read_csv("00extras/milligelir.csv",squeeze=True)
kıta = pd.read_csv("00extras/kıta.csv",squeeze=True)

print(kıta)


#sayma ve sıralama yapma
print(kıta.value_counts())

#sayma sıralama yapma ters sıralama
print(kıta.value_counts(ascending=True))

print(milli)

#indexlerin maksimum versiyonu olan kısmı çeker
print(milli.idxmax())

print(milli[0])

#indexlerin minimum hali çekilir 
print(milli.idxmin())

print(milli[19])

#bir fonksiyon tanımlayıp ona göre kıyas yapma
def sınıf(gel):
    if gel<2000000:
        return "orta"
    elif gel>=2000000 and gel <= 5000000:
        return "yüksek"
    else:
        return "çok yüksek"

s = milli.apply(sınıf)
print(s)
