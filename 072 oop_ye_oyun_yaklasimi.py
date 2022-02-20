import random
class Dusman:
    def __init__(self,isim="dusman",kalan_can=500,saldiri_gucu=10,mermi_sayisi=5): #yapıcı fonksiyon init
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim + " saldırıyor...")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi)+" kadar harcandı")
        self.mermi_sayisi -= harcanan_mermi
        return (harcanan_mermi,self.saldiri_gucu)

    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print(self.isim," vuruldum")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)

    def mermibitti_mi(self):
        if(self.mermi_sayisi <= 0):
            print(self.isim +"konuşuyor : mermim bitti oyundan çıkıyorum")
            return True
        return False

    def print(self):
        print("Basılıyor....................")
        print("isim:",self.isim,"Kalan can :",self.kalan_can,"saldiri gucu :",self.saldiri_gucu,"mermi sayisi :",self.mermi_sayisi)


dusmanlar =[]

i = 0

while(i<10):
    rastgelecan = random.randrange(100,200)
    rastgelesaldirigucu = random.randrange(10,20)
    rastgelemermi = random.randrange(20,30)
    yenidusman =Dusman("Dusman" + str(i+1),rastgelecan,rastgelesaldirigucu,rastgelemermi)
    dusmanlar.append(yenidusman)

    i +=1

i=0
while(i<3):
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)

    donendeger = dusmanlar[randomdusman1].saldir()
    dusmanlar[randomdusman2].saldiriyaugra(donendeger[0],donendeger[1])

    print(" rauund bitti .....")

    i += 1
