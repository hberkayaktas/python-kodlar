class Ogrenci():
    def derscalis(self):
        print("ogrenci şuanda ders çalışıyor")

class calisan():
    def calis(self):
        print("Personel şuanda çalışıyor")

class Yazilimci(Ogrenci,calisan):
    pass

yazilimci =Yazilimci()
yazilimci.derscalis()
yazilimci.calis()