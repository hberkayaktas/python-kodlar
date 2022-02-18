print("Arbitary Arguments Args ")

def topla(*args):
    # * dan sonra Numaralar da diyebilirsin
    # args yazmak zorunda değilsin 
    toplam = 0
    for i in args:
        toplam = toplam + i
    print(toplam)


topla(1,5,8,9,15)
"""" 
içine ne eklenirse eklensin toplama yapan 
fonksiyonlara arbitary arguments
denir 
"""