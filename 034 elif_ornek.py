print("If-elif-else koşul İfadesi örnek")


ders_notu = int(input("Notunuzu girin:"))

if ders_notu >= 90 and ders_notu <=100:
    print("AA aldınız")
elif ders_notu >= 80 and ders_notu <90:
    print("BB aldınız")
elif ders_notu >= 70 and ders_notu <90:
    print("cc aldınız")
elif ders_notu >= 60 and ders_notu <70:
    print("dd aldınız")
elif ders_notu >= 50 and ders_notu <60:
    print("ff aldınız")
elif ders_notu >= 0 and ders_notu <50:
    print("Dersten kaldınız")
else:
    print("geçerli bir değer girin")