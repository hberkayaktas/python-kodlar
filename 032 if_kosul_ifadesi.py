print("If koşul İfadesi")

if 5<3:
    print("bes büyüktür üç")
else:
    print("yanlış")


kullanici_adi = "yang"
sifre = "12345"

ad = input ("Kullanıcı adınızı girin : ")
sifre_gir=input("Şifrenizi adınızı girin : ")


if kullanici_adi == ad and sifre == sifre_gir:
    print("Sisteme girildi")
else: 
    print("Yanlış giriş")