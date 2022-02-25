from operator import ge
import pandas as pd
#pip install pandas

print("PANDAS VERİ TİPLERİ")
x = [1,2,3,5,6]
y=pd.Series(x) #pandas verisine çeviriyoruz
print(y)

ülke = ["abd","çin","kore","rusya"]
ü=pd.Series(ülke) #pandas verisine çeviriyoruz
print(ü)

d=[True,True,False]
y=pd.Series(d) #pandas verisine çeviriyoruz
print(y)

gelir={
    "abd":80000,
    "almanya":90000,
    "türkiye":150000
}
y=pd.Series(gelir) #pandas verisine çeviriyoruz
print(y)

#listenin indeclerini öğrenme
print(ü.index)
#liste değerlerini öğrenme
print(ü.values)

#data tipi öğrenme
print(ü.dtype)

#datanın matris tipini öğrenme
print(ü.shape)

#serinin adını değiştirme
ü.name = "ülkeler"
print(ü)

#serinin ilk sayılarını alırız içine bir şey 
#yazmaz isek ilk beş ifadeyi çeker
print(ü.head()) 



