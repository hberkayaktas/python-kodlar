dersler={"Ahmet":["Veri tabanları","işletim sistemleri"],"oğuz":["script dersi","nesne tabanlı programlama"],"sinan":["lineer algebra"]}

isim = input("isim giriniz:")

print("{} in aldığı dersler".format(isim))

for i in (dersler[isim]):
    print(i)