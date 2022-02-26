import pandas as pd

oyun= pd.read_csv("00extras/wcplayers.csv",index_col="FIFA Popular Name")
print(oyun)

takım = oyun.groupby("Team")
print(takım)


#satır değeri okuma
print(len(oyun))
print(len(takım))

#ilk değerler alınır
print(takım.first())

#son değerler alınır
print(takım.last())

#brazil grubunu çekme ve yazma
print(takım.get_group("Brazil"))

#2
print(takım.get_group("France"))

#tablodaki maksimum değerleri bulur
print(takım.max())

#tablodaki minimum değerleri bulur
print(takım.min())

#toplama yapma
print(takım.sum())

#ortalama bulma
print(takım.mean())

takım = oyun.groupby(["Team","Club"])
print(takım)

#boyut ve dağılım öğrenme
print(takım.size())

#belirli indexleri çağırma
tak = takım.agg({"Height":"sum",
        "Weight":"mean"
        })
print(tak)

takım = oyun.groupby("Team")

#stun başlıklarını alma
df =pd.DataFrame(columns=oyun.columns)
print(df)

for ülke,data in takım:
    uzun = data.nlargest(1,"Height")
    df= df.append(uzun)

print(df)