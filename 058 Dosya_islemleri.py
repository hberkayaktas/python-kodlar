from statistics import mode


print("Dosya işlemleri")

dosya = open("dosya.txt",mode="w",encoding="utf-8")
#yazma modu w
dosya.write("Zaman Çarkı, Amazon Prime Video\naracılığıyla  yayınlanan bir\nAmerikan epik fantezi televizyon dizisidir.")

#dosya.close()

dosya = open("dosya.txt",mode="a",encoding="utf-8")
#add modunda açılıyor
dosya.write("\nRobert Jordan'ın aynı adlı\nroman serisinden uyarlanan dizinin\nyapımcılığını Sony Pictures\nTelevision ve Amazon Studios\nüstleniyor ve yapımcılığını \nRafe Judkins üstleniyor.")
#ekleme yapılıyor varsa yazmaz
#dosya.close()

dosya = open("dosya.txt",mode="r",encoding="utf-8")

for i in dosya:
    print(i)

#veya satır satır okuma
dosya.readline()

#dosyayı kendi  açıp kendi  kapıyor buffer kendiliğinden 
# serbest kalıyor
#dosya.seek(10)  10 harf atlayıp veriçekicek
# print(dosya.read())
dosya.seek(10)
#10 karakter git
str1 = dosya.read(5)
#5 karakterlik veri çek
dosya.seek(15)
#15 karakter git
str2 = dosya.read(5)
#5 karakter veri çek

print(str1,str2)


#dosya daki  satırları bir listeye atama ve yazdırma
liste = dosya.readlines()
print(liste[1])

with open("yazilim.txt","r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"PHP : Rasmus liedorf22\n")
    dosya.seek(0)
    dosya.writelines(data)

with open("yazilim.txt","r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"PHP : Rasmus liedorf22\n")
    dosya.seek(0)
    dosya.writelines(data)