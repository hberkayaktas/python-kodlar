import pandas as pd

world = pd.read_csv("00extras/wcplayers.csv")

print(world)

#takım indexini ve shirtname indexini kullanılacağını belirttik
ss = world.set_index(keys=["Team","Shirt Name"])
print(ss)

#çağırdığımızda önceki  index de gelir
print(ss.iloc[2])

#index sıralama
ss = ss.sort_index()
print(ss)

#index başlıklarını öğrenme
print(ss.index.names)

#index elementlerini çekme
print(ss.index[1])

#tüm stunu çekme
print(ss.index.get_level_values(1))

#index ismi değiştirme
tr = ss.index.set_names(["TAKIM","TAKMA İSİM"],inplace=True)
print(ss)

#stun içi sıralama yapma false ters true düz sıralar
print(ss.sort_index(ascending=[False,True]))

#index atlama
print(ss.swaplevel())

# tablodaki  verileri box by box şeklinde okutma
print(ss.stack())

#bir pencere içerisinde okuma
print(ss.stack().to_frame())

#tüm tabloyu çözme
print(ss.unstack())
