from operator import sub
import pandas as pd

df= pd.read_csv("00extras/millitakım.csv")
print(df)


print("#milyon euro değeri float haline getiriliyor")
df["Milyon Euro"] = df["Milyon Euro"].astype("float")
print(df)


print("#aralık bulma")
yaş = df["Yaş"].between(20,25)
print(df[yaş])

print("#2")
değ = df["Milyon Euro"].between(5.0,20.0)
print(df[değ])

print("#tablyu veya stunu kopyalamak ")
df1 = df["Görev"].duplicated()
print(df[df1])

print("#görev değişkenlerindeki son değerlerden yeni bir tablo oluşturur")
df2 = df["Görev"].duplicated(keep="last")
print(df[df2])

print("ilk rastlanılan görev dep. harici olanları çıkarıcağız")
df3 = df.drop_duplicates("Görev")
print(df3)

print("görev dep. sondeğerleri harici çıkarıcağız")
df4 = df.drop_duplicates(subset='Görev',keep='last')
print(df4)


print("bir değişken üzerindeki eşsiz değerleri gösterir")
dfs = df["Görev"].unique()
print(dfs)

print("sütundaki eşsiz karakter sayısını öğrenme")
print(len(df["Görev"].unique()))

print("sütundaki eşsiz olmayan karakter sayısını öğrenme")
print(df["Görev"].nunique())


