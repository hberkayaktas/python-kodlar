import pandas as pd

altı = pd.read_csv("00extras/2006 wc.csv")
on = pd.read_csv("00extras/2010 wc.csv")
ondört = pd.read_csv("00extras/2014 wc.csv")
onyedi = pd.read_csv("00extras/fifa2017.csv",index_col="Ülke")
onsekiz = pd.read_csv("00extras/fifa2018.csv",index_col="Ülke")
kon7 = pd.read_csv("00extras/fifa2017k.csv")
kon8 = pd.read_csv("00extras/fifa2018k.csv")


#iki veri tabanını birleştirir ve index leri görmezden gelir
kk = pd.concat([ondört,on],ignore_index=True)
print(kk)

#iki dataya da ek stun şeklinde üst index ekler
kk = pd.concat([ondört,on],keys=["2014","2010"])
print(kk)

#yeni indexlenen veriden belirli satırı çekme
x = kk.loc["2014",2]
print(x)


#bir tabloya diğerini ekleme
yy = on.append(altı,ignore_index=True)
print(yy)

#iki tablonun kesişim kümesini ve stun başlığını tanımlama
oo = on.merge(altı,how="inner",on="Futbolcu",suffixes=("-2010","-2006"))
print(oo)

# iki tablonun birleşim olmayan kümesini ve stun başlığını tanımlama
tt = on.merge(altı,how="outer",on="Futbolcu",suffixes=("-2010","-2006"))
print(tt)

#birleştirme örneği
uru = onyedi.merge(onsekiz,how="inner",on="Ülke",suffixes=("-2017","-2018"))
print(uru)

#başka şekilde birleştirme
#rsuffix sağdakilere 
#l suffix soldakilere tablo başlığı ekler
#join in mergeden farkı biri dahil(join) eder diğeri kaynaştırır 
uru2 = onyedi.join(onsekiz,how="outer",lsuffix='ikibin17',rsuffix='ikibin18')
print(uru2)

#onyedi tablosu solda olmak şartıyla iki tabloyuda birleştirir
pp = onyedi.merge(kon7,how="left",on="Ülke")
print(pp)

