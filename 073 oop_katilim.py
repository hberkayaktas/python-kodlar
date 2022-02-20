class Calisan():
    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfın yapıcı fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("çalışan bilgileri gösteriliyor...")
        print("İsim",self.isim,"Maaş:",self.maas,"çalıştığı departman:",self.departman)

    def maasazamyap(self,zam_miktari):
        print("Maaşa Zam yapıldı")
        self.maas += zam_miktari

    def deparmandegistir(self,yeni_departman):
        print("departman değiştiriliyor...")
        self.departman = yeni_departman

class Yonetici(Calisan): #Calisan classından tüm değişkenleri devir al
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("Yönetici sınıfının yapıcı fonksiyonu")
        super().__init__(isim,maas,departman,)
        #super fonksiyonu ile aldık
        #self.isim = isim
        #self.maas = maas
        #self.departman = departman
        self.kisi_sayisi = kisi_sayisi #ek özellik
    def bilgilerigoster(self):
        print("Yönetici sınıfının bilgileri gösteriliyor...")
        print("isim:",self.isim,"Maaş:",self.maas,"Çalıştığı departman:",self.departman,"Kişi sayısı:",self.kisi_sayisi)
    def kisisayisiartir(self,artir):
        print("kişi Sayısı Artırılıyor....")
        self.kisi_sayisi += artir

    #pass

yonetici = Yonetici("Mehmet Baltacı",2500,"İnsan Kaynakları",20) #kalıtım yaparak deviral

yonetici.bilgilerigoster()
yonetici.kisisayisiartir(10)
yonetici.bilgilerigoster()