import pandas as pd

df= pd.read_csv("00extras/millitakım.csv")
print(df)

#belli bir stunu index gibi kullanma
df = df.set_index("İsim")
print(df)

#indexleme işlemini geri alma
df = df.reset_index()
print(df)

#farklı yöntemle indexleme yapma
df = pd.read_csv("00extras/millitakım.csv",index_col="Numara")

#belirli bir satırı çekme
print(df.loc[3])


#veya isimle çağırma (değer ile çağırma)
df = df.set_index("İsim")
print(df.loc["Harun Tekin"])

#aralık olarak alma
print(df.loc["Harun Tekin":"Kaan Ayhan"])

#iloc fonk. ile çağırma
print(df.iloc[0])

print(df.iloc[0:5])
