faktoriyel=1

while True:
    sayi = int(input("lütfen negatif olmayan bir sayi giriniz:"))
    if (sayi  <=0):
        print("lütfen negatif olamayan bir sayı giriniz.")
    else :
        for i in range(1,sayi+1):
            faktoriyel *= i
        print(*range(1,sayi+1))
        print("faktoriyel",faktoriyel)
        break