def geometri(sekil):
    if len(sekil)==3:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]

        if (a+b)>c and (a+c)>b and (b+c)>a :
            if (a==b) and (a==c) and (b==c):
                print("Eşkenar üçgen")
            elif ((a==b) and (a==c)):
                print("ikizkenar üçgen")
            else:
                print("çeşitkenar üçgen")
        else:
            print("üçgen belirtmiyor")


    elif len(sekil) == 4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]

        if (a==b) and (a==c) and (a==d):
            print("kare")
        elif (a== c) and (b==d):
            print("dikdörtgenler")
        else:
            print("normal dörtgen")

    else:
        print("herhhangi bir şekil değil")



while True:
    eleman_sayisi = int(input("eleman sayisinı giriniz :"))
    if (eleman_sayisi == 3):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        geometri([a,b,c])

    elif (eleman_sayisi == 4):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d:"))
        geometri([a, b, c, d])

    else:
        print("tekrar giriniz")