print("Nesne tabanlı Programlama")

#sınıflar birden çok kullanılmak üzüre
#yazılmış nesne şablonlarıdır


#tek kullanımlık sınıf tanımlama 
class Ogrenci:
    isim = "berkay"
    soyisim ="aktaş"
    yaş = 19
    not_ort = 85


bir = Ogrenci() #sınıfı değişkene atarız

#atanan değişkeni çağırma
print(bir.isim)
print(bir.soyisim)
print(bir.not_ort)
print(bir.yaş)


#yapısal sınıf oluşturma
#initializer or constructor
#__init__() fonksiyonu yapısal  class oluşturmaya yarar
#yapısal classlar içinde birden fazla öğe tanımlaması
# yapılarak nesneler oluşturulabilir

class Ogrenci:
    def __init__(self,isim,soyisim,yaş,not_ort):
        self.nesnenin_ismi = isim
        self.nesnenin_soyismi =  soyisim
        self.nesnenin_yaşı = yaş
        self.nesnenin_not_ort = not_ort

bir = Ogrenci("berkay","aktaş",25,90)
iki = Ogrenci("jennifer","lawrence",30,75)

print(bir.nesnenin_ismi)
print(iki.nesnenin_soyismi)



#class içi fonksiyon çağırma 
class Ogrenci:
    def __init__(self,isim,soyisim,yaş,not_ort):
        self.ismi = isim
        self.soyismi =  soyisim
        self.yaş = yaş
        self.not_ort = not_ort

    def info(self):
        print("{} {} {} yaşında ve {} notu olan bir öğrencidir".format(self.ismi,self.soyismi,self.yaş,self.not_ort))

bir = Ogrenci("berkay","aktaş",25,90)
iki = Ogrenci("jennifer","lawrence",30,75)

bir.info()
iki.info()


#class içi fonksiyon return ve bilgi yazdırma

class Ogretmen:
    def __init__(self,isim,soyisim,yaş,maaş,uzmanlık):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.maaş = maaş
        self.uzmanlık = uzmanlık

    def info(self):
        print(
        """
        isim = {}
        soyisim = {}
        yaş = {}
        maaş = {}
        uzmanlık = {}
        """.format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

    def zam(self):
        return self.maaş*1.3 

uc = Ogretmen("berkay","aktaş",35,5000,"fizik")
uc.info()
print(uc.zam())
