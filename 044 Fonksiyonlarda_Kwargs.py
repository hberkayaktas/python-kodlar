

from multiprocessing.sharedctypes import Value

def jenni(**kwargs):
    for key in kwargs.keys():
        print("anahtarlar: ",key)

print(jenni(isim="nuri",soyisim="şahin"))


def kimlik(**kwargs):
    for key,Value in kwargs.items():
        print("{}={}".format(key,Value))
        print("anahtarlar: ",key)
        print("karşılıklar: ",Value)

kimlik(isim = "mehmet",soyisim ="tek",yaş =29 ,tc= 135646645, email="hkadksa@glga.com",anneadi="huriye")



def yeni (*args,**kwargs):
    print("args :",args,"kwargs:",kwargs)

yeni(1,2,3,4,5,6,isim="berkau",soyisim="aktaş")



def birlestir(**kwargs):
    son = ""
    for kelime in kwargs.values():
        son = son + kelime
    return son

print(birlestir(a = "python ", b="dünyanın ",c="ençok kukkalınal dilidir"))