def factoriyel(numara):
    faktoriyel =1
    for i in range(1,numara+1):
        faktoriyel *=i
    #print("faktoriyel",faktoriyel)
    return faktoriyel


sayi = int(input("sayi giriniz:"))

a = factoriyel(sayi)

print(a)