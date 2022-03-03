import pandas as pd

futbol = pd.read_csv("00extras/pivot.csv")
print(futbol)

#indexi ve  stunlar yeniden tanımlanır değerler de gol değerleridir
x = futbol.pivot(index="Futbolcu",columns="Mevsim",values="Gol")
print(x)

#gol stunu altında tümünü toplama
toplama = futbol.pivot_table(index="Futbolcu",values="Gol",aggfunc="sum")
print(toplama)

#gol stunu altında tümünün ortalamasını alma
ortalama = futbol.pivot_table(values="Gol",index="Futbolcu",aggfunc="mean")
print(ortalama)

#melt.csv çağırılır
meltdeneme = pd.read_csv("00extras/melt.csv")
print(meltdeneme)

#tablonun değerlerini index doğrultusunda dağıtma
melted = pd.melt(meltdeneme,id_vars="Futbolcu",var_name="Yıl",value_name="Gol")
print(melted)
