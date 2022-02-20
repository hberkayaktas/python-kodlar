class Dusman:
    def __init__(self,isim="dusman",kalan_can=500,saldiri_gucu=10,mermi_sayisi=5): #yapıcı fonksiyon init
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def print(self):
        print("Basılıyor....................")
        print("isim:",self.isim,"Kalan can :",self.kalan_can,"saldiri gucu :",self.saldiri_gucu,"mermi sayisi :",self.mermi_sayisi)


dusman1 = Dusman("Ali",2000,30,50)
dusman2 = Dusman("Veli",1000,20,40)
dusman3 =Dusman()

print("Dusşman1**********************************")
dusman1.print()
print("Dusşman2**********************************")
dusman2.print()
print("Dusşman3**********************************")
dusman3.print()