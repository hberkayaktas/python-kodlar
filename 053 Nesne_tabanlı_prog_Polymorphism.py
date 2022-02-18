print("Nesne tabanlı Programlama 5")
#Polymorphism (Çok Şekillilik , Çok Biçimlilik)


class Okul:
    def __init__(self,isim,soyisim,yaş,maaş):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.maaş = maaş
        print("okul sınıfı çalıştı1")

    def info(self):
        print("{} {} {} yaşında ve {} maaşı olanbir okul üyesidir.".format(self.isim,self.soyisim,self.yaş,self.maaş))
    
    def zam(self):
        return self.maaş * 1.2

class Ogretmen(Okul):
    def __init__(self, isim, soyisim, yaş, maaş,uzmanlık):
        super().__init__(isim, soyisim, yaş, maaş)
        self.uzmanlık = uzmanlık
        print("Öğretmen sınıfı çalıştı")
    
    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir {} Öğretmenidir.".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))
    
    def zam(self):
        return self.maaş * 1.5

class Yonetim(Okul):
    def __init__(self, isim, soyisim, yaş, maaş):
        super().__init__(isim, soyisim, yaş, maaş)
        print("Yönetim sınıfı çalıştı")

    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir yönetim görevlisidir.".format(self.isim,self.soyisim,self.yaş,self.maaş))

    def zam(self):
        return self.maaş * 2

bir = Okul("semih","saygın",36,6000)
iki = Ogretmen("Kemal","çelik",45,6000,"kimya")
uc = Yonetim("burak","yilmaz",55,6000)

#print(bir.zam())
bir.info()

#print(iki.zam())
iki.info()

#print(uc.zam())
uc.info()