import numpy as np
#pip install numpy


print("#Numpy ve arrayler")
ww= np.arange(10)
#bir aralık tanımlar 0-9 arası dizi TEK BOYUTLU
print(ww)

ww2= np.arange(10)**2
print(ww2)
##tüm serinin karesini alır

print(ww2[3])
#3. index i çağırıyor

print(ww2[3:6])
#3-6 arasındaki indexleri çağırıyor

ww2[4] = 1000
#index değeri değiştirme
print(ww2)

for i in ww2:
    print(i*2)


print("#çok boyutlu array")


#çok boyutlu array
y = np.random.random(16) #0-1 arasında 16 sayılık matris oluşur
print(y)

y = y.reshape(4,4)
#yeniden sekillendirilir
#4,4 boyutlu bir matris oluşturulur
print(y)

y = y.ravel()
#şekil tekrar dizi haline gelir
print(y,"şekil tekrar dizi haline geldi")

y = y.reshape(4,4) #tekrar 4x4 matris oluşturuluyor


print(y[0:2],"0-2 ilk iki satır")
#0-2 ilk iki index çağırılıyor

print(y[0:2,1],"0-2 ilk iki satır 2 stun ")
#0-2 ilk iki index çağırılıyor

print(y[:,3],"4. sutun ")
#4.sutun çağırılır


#for döngüsü ile matris okuma
print("for döngüsü ile çağırır")
for satır in y:
    print(satır)


print("----for döngüsü ile index index okuma----")
for satır in y.flat:
    print(satır)

print("----for döngüsü denumere etme index öğrenme----")
for satır in np.ndenumerate(y):
    print(satır)

a = np.array([2,3])
b = np.array([5,6])

print("iki matrisi yatay toplama")
z = np.hstack((a,b))
print(z)

print("iki matrisi dikey toplama")
z = np.vstack((a,b))
print(z)

print("iki matrisi birleştirme")
g = np.array([[1,2],[3,4]])
t = np.array([[5,6]])

j= np.concatenate((g,t),axis=0)
print(j)

print("transpose ve birleştirme")
k= np.concatenate((g,t.T),axis=1)
print(k)

print("#matrislerle çalışma")

x = np.array([1,2,3,4])
#listenin tipini öğrenme
print(type(x))

x = np.zeros((3,4))
#3 satır 4 sutun 0 matrisi
print(x)

t = np.ones((2,4))
#2 satır 4 stun birim matris
print(t)

t = np.ones((2,4))*5
#2 satır 4 stun 5 matrisi
print(t)

n = np.arange(10,50,5)
#aralık tanıtımı 10 dan başla
#50 ye kadar 5 er beşer artır
print(n)

ondalıklı = np.arange(0,2,0.2)
#0 dan 2ye 0.2 artır
print(ondalıklı)

lin = np.linspace(0,4,12)
#0 dan 4 e 12 tane sayı
print(lin)

rast = np.random.rand(3,4)
#3 satır 4 stun 0-1 aralığında 12 sayı
print(rast)

rast2 = np.random.randn(2,5)
#2 satır 5 stun -1-1 aralığında 12 sayı
print(rast2)

fonksiyoncarpma = np.random.randn(2,5)*5
print(fonksiyoncarpma)

ff= np.eye(5)
#kösegen matris
print(ff)

y = np.arange(24)
#0 dan 24 e kadar dizi oluşturur
print(y)

y_yeni= y.reshape(6,4)
#6 satır 4 stunlu yeni bir matris olusturur
print(y_yeni)

y_yeni2 = y.reshape(2,3,4)
#3x4x2 lik 3 boyutlu matris oluşur
print(y_yeni2)

aa= y_yeni2.max()
#maksimum ifadeyi verir
print(aa)

aa2= y_yeni2.min()
#min ifadeyi verir
print(aa2)

aa3 = y_yeni2.argmin()
print(aa3)

aa3= np.arange(50)
#dizinin boyutlarını verir
aa3.shape = 2,-1,5
print(aa3)
print(aa3)



print("#Numpy İşlemler")
s = np.array([20,40,60,80])
print(s)

b = np.arange(4)

c = s+b
print("matris toplamı",s)

print("karesi alınmış",s**2)
print("mantıksal işlemler 50 den büyükmü?",s>50)
s= s+10
print("tümüne 10 ekleme",s)

#karma dizi oluştur 12 karakterli 
v = np.random.random(12)
print(v)
print("dizinin maksimumu:",v.max())
print("dizinin minimumu:",v.min())
print("dizinin toplamı:",v.sum())

b = np.arange(15).reshape(3,5)
print(b)
print("Dikey toplama",b.sum(axis=0))
print("Diziyi yatay toplama",b.sum(axis=1))
print("Dizideki maximum",b.max(axis=1))
print("",b.cumsum(axis=1))

k= np.random.random(10)
print(k)
print("Ortalama",k.mean())
print("medyan",np.median(k))
print("standart sapma",np.std(k))
print("dizinin varyansı",np.var(k))

#bir diziyi kopya etme
kopya = k.copy()
print(kopya)

şehir = np.array(["ankara","istanbul","bursa","ankara","izmir","bursa","izmir"])
print(şehir)







