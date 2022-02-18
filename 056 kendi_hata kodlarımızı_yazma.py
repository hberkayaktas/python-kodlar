from multiprocessing.sharedctypes import Value


try:
    x = int(input("bir sayı giriniz :"))
    y = int(input("ikinci sayısı giriniz :"))
    print(x/y)


#except :
#    print("hata oluştu :") 
#eğer herhangibir spesifik hata tanımlamayacaksak bunu
#kullanılabilir


except ValueError:
    print("lütfen bir sayı giriniz")

except TypeError:
    print("Verilerin tipinde hata var")
    #eğer değişken tanımlarken int yazmazz isek bu hatayı alırız

except ZeroDivisionError:
    print("0 dan farklı bir değer giriniz")

else:
    print("program problemsiz çalıştı")

finally:
    print("Program finali")


    
