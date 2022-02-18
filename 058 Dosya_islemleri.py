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
