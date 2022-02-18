print("Nesne tabanlı Programlama 4")

class Okul:
    def __init__(self,isim,soyisim,yaş):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        print("okul sınıfı çalıştı1")

    def info(self):
        print("{} {} {} yaşında bir okul üyesidir.".format(self.isim,self.soyisim,self.yaş))

class Ogretmen(Okul):
    def __init__(self, isim, soyisim, yaş,maaş,uzmanlık):
        super().__init__(isim, soyisim, yaş)
        self.maaş = maaş
        self.uzmanlık = uzmanlık
        print("Öğretmen sınıfı çalıştı")
    
    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir {} öğretmenidir".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

bir = Okul("ali","sağlam",35)
iki = Ogretmen("mustafa","yıldız",35,4000,"türkçe")

bir.info()
iki.info()
