
print("Hata tanımlaması")

#input için hata tanımlaması yazma
x = int(input("bir sayı girimiz :"))
class SıfırHatası(Exception):
    pass

if x == 0:
    #raise Exception("lütfen 0 dan farklı bir değer giriniz.")
    raise SıfırHatası("lütfen 0 dan farklı bir değer giriniz.")
else:
    print(x)

