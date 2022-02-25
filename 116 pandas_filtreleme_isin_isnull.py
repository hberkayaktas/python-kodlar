import pandas as pd

df= pd.read_csv("00extras/millitakım.csv")
print(df)


#filtrasyon yapma görevi on numara olan oyuncular filtrelenir
görev = df["Görev"] == "on numara"
print(df[görev])

#2
ayak = df["Ayak"] == "sol ayak"
print(df[ayak])


#çift filtre yapma
print(df[ayak & görev])

#büyüklükğe göre filtreleme
yaş = df["Yaş"]>25
print(df[yaş])

#Veya filtresi
print(df[yaş | görev])

print(df[yaş & görev | ayak])


k = df["Takım"].isin(["Başakşehir","Kayseri"])
print(df[k])

#gol değeri Boş olan oyuncular
null = df["Gol"].isnull()
print(df[null])

#gol değeri boş olmayan değerler tablodan çekilir
notnull = df["Gol"].notnull()
print(df[notnull]) 
