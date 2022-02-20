class Dusman:
    kalan_can =3
    def saldir(self):
        print("hucuuuuuuuum")
        self.kalan_can -=1

    def hayatta_mi(self):
        if(self.kalan_can <= 0):
            print("Öldü")
        else:
            print(str(self.kalan_can)+" canım kaldı")


dusman1 = Dusman()
dusman2 = Dusman()

dusman1.saldir()
dusman1.saldir()
dusman1.hayatta_mi()


dusman2.saldir()
dusman2.saldir()
dusman2.saldir()
dusman2.hayatta_mi()
