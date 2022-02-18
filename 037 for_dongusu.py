print("For dögüsü")

sai = [1,2,4,6,8,9,10,13,15]

print(1 in sai)

for sayi in sai:
    print("sayiniz :",sayi)
    if sayi == 10:
        break #10 dan sonra sayma
    #eğer continue olursa 10 u atlayıp devam eder
else:
    print("Döngü bitti")

