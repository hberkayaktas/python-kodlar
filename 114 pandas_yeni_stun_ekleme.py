import pandas as pd

dünya = pd.read_csv("00extras/dünya.csv")
print(dünya.head())

#sadece ülke stununu çağıralım
print(dünya[["Ülke"]].head())

#sadece ülke ve kıta stunlarını çekme
print(dünya[["Ülke","KITA"]].head())

#yeni stun ekleme
qq = dünya["Sıralama"] = "tpo 20"
print(dünya)

#farklı şekilde ekleme
ss = dünya.insert(2,column ="gelir düzeyi",value="yüksek gelir")
print(dünya)

#tüm stun üzerinde çalışma
ww = dünya["Gelir"]= dünya["Gelir"] /1000000
print(dünya)

#yeni bir satırı var olan satır üzerinden işlem yapark tanımlama
ww = dünya["Gelir Türk Lirası"]= dünya["Gelir"] *4.48
print(dünya)

#sutun üzerinde kelime frekansı ölçme
ww= dünya['KITA'].value_counts()
print(dünya)


