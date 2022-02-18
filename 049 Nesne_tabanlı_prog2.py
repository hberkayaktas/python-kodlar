print("Nesne tabanlı Programlama 2")

#Encapsulation — Kapsülleme (Erişimi Engelleme)
#kapsülleme işlemi __degisken şeklinde olur


class Ogretmen:
    def __init__(self,isim,soyisim,yaş,maaş,uzmanlık):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş #genel değişken
        self.__maaş = maaş  #özel değişken dışarıdan erişilemez
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
    
    def getMaas(self):
        return self.__maaş
        #bu fonksiyon vasıtası ile kapsüllenmiş işlem 
        # çalışır hale gelir
    def setMaas(self,yeni_maas):
        self.__maaş = yeni_maas
        #yeni maaşın atama fonksiyonu
    
    def __yas_degis(self,yeni_yas):
        self.yaş = yeni_yas 
        return self.yaş   

uc = Ogretmen("berkay","aktaş",35,5000,"fizik")
print(uc.yaş) #bu sorgu çalışır
#print(uc.__maaş) #bu sorgu çalışmaz çünkü kilitli

uc.getMaas()
print(uc.getMaas())
#eski maas çağırılır

uc.setMaas(10000)
print(uc.getMaas())
#yeni maaş tanımlanır

print(uc.__yas_degis(12))
print(uc.yas_degis(12))
#bu şekilde metoda erişim engellenir



