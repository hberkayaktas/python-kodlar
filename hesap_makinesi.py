print("modül yazma ve dahil etme")
#Hesap makinesi

def topla(*args):
    toplam= 0 
    for i in args:
        toplam = toplam + i
    return toplam
