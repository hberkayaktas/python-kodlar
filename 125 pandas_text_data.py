from unicodedata import category
import pandas as pd

kupa = pd.read_csv("00extras/wcplayers.csv")
print(kupa)

print(kupa.info())

#team değeri category olarak tanımlanıyor
kupa["Team"] = kupa["Team"].astype("category")
print(kupa["Team"])

#sayısını öğreniyoruz
print(kupa["Team"].nunique())

#index deki isimleri büyültme 
print(kupa["FIFA Popular Name"].str.upper())


#index deki isimleri küçültme 
print(kupa["FIFA Popular Name"].str.lower())

#index deki isimlerin sadece baş harfleri büyütme
print(kupa["FIFA Popular Name"].str.title())

#index deki isimlerin karakter uzunluğunu bulma
print(kupa["FIFA Popular Name"].str.len())

#index deki isimleri değiştirme
fi = kupa["Team"].str.replace("Argentina","ARGENTİNA")
print(fi)

#farklı örnek
ornek = kupa["Birth Date"].str.replace(".","/")
print(ornek)

print(kupa)

#bu kod ile stunlarda belirli değeri arar var ise True yoksa false bool 
#ifadesi geri döndürür
fi = kupa["FIFA Popular Name"].str.lower().str.contains("manuel")
print(fi)
#sorgu olarak atama
#isminde manuel olanları döndürür
print(kupa[fi])

#startswith man deyince man ile başlayan indexleri bulur
man = kupa["FIFA Popular Name"].str.lower().str.startswith("man")
print(kupa[man])

#endwith uel deyince uel ile biten indexleri bulur
uel = kupa["FIFA Popular Name"].str.lower().str.endswith("uel")
print(kupa[uel])

grlt = "        Ejderha Smaug    "
print(grlt.lstrip().rstrip())
print(grlt.strip())

kupa["FIFA Popular Name"] = kupa["FIFA Popular Name"].str.strip()
print(kupa["Club"].str.strip())
