print("Nested if")

if 5 > 3 : print("5 büyüktür 3")#tek satırda if

print("5 büyüktür 3") if 1>3 else print("yanlış")

#teksatırda if ifadesi 

sayi = int(input("bir sayı giriniz:"))

if sayi >= 0:
    if sayi == 0:
        print("sayi sifirdir")
    else:
        print("sayi pozitif")
else:
    print("sayi negatiftir")

