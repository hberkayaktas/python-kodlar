import pandas as pd

df= pd.read_csv("00extras/millitakım.csv",index_col="İsim")

print(df)

#örnek veri çekme
print(df.sample(5,axis=0))

#sıralama yapma
print(df["Yaş"].sample(5,axis=0).sort_values())

#df tablosundaki en küçük değerli 3 veriyi çekme
print(df.nsmallest(3,columns="Yaş"))

#df tablosundaki en büyük değerli 5 veriyi çekme
print(df.nlargest(5,columns="Yaş"))


#tabloda arama yapma where ile aranılan nesne harici NaN olur
sorgu = df["Takım"] == "Fenerbahçe"
print(df.where(sorgu))


#koşullu sorgu harici NaN olur
yaş = df["Yaş"]<30
print(df.where(yaş))

#ikili sorgu harici NaN olur
print(df.where(sorgu & yaş))

#sadece istenen değerlerde bir tablo çağırır
print(df.query('Takım == "Fenerbahçe"'))

#başka bir sorgu
print(df.query('Görev == "sol bek"'))

#mantıksal sorgulama
print(df.query('Yaş > 25'))


#for döngüsü ile tüm tablo üzerinde değişiklik yapma ve uygulama
def milyon(number):
    return str(number) + " milyon euro"

sütun = ["Milyon Euro"]
for satır in sütun:
    df[satır] = df[satır].apply(milyon)

print(df)

#tablo kopyalama
takımlar = df["Takım"].copy()
print(takımlar)
#kopyalanan tabloda değişiklik yapma ama değişiklik 
#ana df tablosunda uygulanmaz
takımlar["Harun Tekin"] = "Türkiye"
print(takımlar)
