print("Demetler - Tuple")

dems =("ben","sen","o","siz","biz")
print(dems[0])

# demetlere ekleme çıkarma yapılmaz
#dems[0] = "nuri"

print(dems[-3:-1]) #indexlene bilir
print(dems[0:3]) 

print(len(dems))

sayilar= (1,2,3,5,5,6,5,1,5)

print(sayilar+dems) #demetler toplanabilir

print(sayilar.count(5)) #sayıcı kullanılabiir
print(sayilar.index(3)) #indec sorgulaması yapılıtor

#tekelemanlı bir demet tanımlamak için
t = (4,)
