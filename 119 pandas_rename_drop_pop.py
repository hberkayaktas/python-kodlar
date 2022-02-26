from os import rename
import pandas as pd

df= pd.read_csv("00extras/millitakım.csv",index_col="İsim")
print(df)


#dördüncü index çağırılıyor
print(df.iloc[4])

# sıfırıncı sütun 4 satır değiştir
df.iloc[4,0] = 100
print(df)

# 0. sütun 4,5,6 . satırları değiştirir 
df.iloc[[4,5,6],0] = [1000,2000,3000]
print(df)

#filtre tanımlama ve filtrelenenen öğeleri editleme
f = df["Görev"] == "kaleci"
df.loc[f,"Görev"] = "KALECİ"

print(df)

#stun ismi değiştirme
df = df.rename(columns={"Görev":"Mevki","Maç":"Maç Sayısı"})
print(df)

#index yedinen isimlendirme
df = df.rename(index={"Kaan Ayhan":"KAAN AYHAN"})
print(df)


#bazı sütunlar olmadan tabloyu alma
df = df.drop(labels=["Maç Sayısı","Gol"],axis=1)
print(df)

#indexi ve belirli stun ile çağırma
df = df.pop("Yaş")
print(df)

