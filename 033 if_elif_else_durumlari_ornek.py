print("If-elif-else koşul İfadesi")

kullanici_adi = "yang"
sifre = "12345"

ad = input ("Kullanıcı adınızı girin : ")
sifre_gir=input("Şifrenizi adınızı girin : ")


if kullanici_adi == ad and sifre == sifre_gir:
    print("Sisteme girildi")
elif kullanici_adi != ad:
    print("kullanıcı adı yanlış") 
else: 
    print("Yanlış giriş")

    