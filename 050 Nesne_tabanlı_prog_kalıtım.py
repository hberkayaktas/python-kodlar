print("Nesne tabanlı Programlama 3")

#2.Inheritance ( Kalıtım )
#başka bir classtan miras alma

class Okul:
    def __init__(self,isim,soyisim,yaş):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        print("okul sınıfı çalıştı")

class Ogretmen(Okul):
    def __init__(self, isim, soyisim, yaş):
        super().__init__(isim, soyisim, yaş)
        print("Öğretmen sınıfı çalıştı")
        #super() fonksiyonu ile miras alırız.
    
    def info(self):
        print("{} {} {} yaşında bir öğretmenidir.".format(self.isim,self.soyisim,self.yaş))

bir = Ogretmen("ali","yılmaz",35)

bir.info()



class Ogretmen2(Okul):
    def __init__(self, isim, soyisim, yaş,maaş,uzmanlık):
        super().__init__(isim, soyisim, yaş)
        self.maaş = maaş
        self.uzmanlık = uzmanlık
        print("öğretmen 2 sınıfı çalıştı")
        #kalıtımı alıp ekstra özellik ekleriz
    
    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir {} öğretmendir.".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

    def zam(self):
        return self.maaş * 1.5

iki = Ogretmen2("cemil","durmaz",35,6000,"matematik")
iki.info()
iki.zam()


class Ogrenci(Okul):
    def __init__(self, isim, soyisim, yaş,not_ort):
        super().__init__(isim, soyisim, yaş)
        self.not_ort = not_ort
        print("Öğrenci sınıfı çalıştı")

    def info(self):
        print("{}{}{}yaşında ve not ortalaması {} olan bir öğrencidir".format(self.isim,self.soyisim,self.yaş,self.not_ort))

ogr_bir = Ogrenci("Cemil","Meriç",18,75)

ogr_bir.info()
