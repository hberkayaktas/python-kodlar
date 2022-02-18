# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Sözlüklerin metodlari - metods of Dictionary")
#sozluk tanımlama
kimlik = {
    "isim":"hakan",
    "Soyisim":"menguc",
    "yas":19,
    "yer":"duzce",
}
#sozluk anahtarları
print(kimlik.keys())
#sozluk degerleri
print(kimlik.values())
#tum elemanlar
print(kimlik.items())
#belirli ifade alma (sadece anahtarla calisir)
print(kimlik.get("Soyisim"))
#sozluğe ifade ekleme
kimlik.update({"anne_adı":"emilie"})
print(kimlik)
