# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Sözlükler - Dictionary")
#sozluk tanımlama
kimlik = {
    "isim":"hakan",
    "Soyisim":"menguc",
    "yas":19,
    "yer":"duzce",
}

#index değitirme
kimlik["isim"] = "jonathan"
print(kimlik)
#uzunluk öğrenme
print(len(kimlik))
#yeni icerikekleme
kimlik["yil"] = 1997
print(kimlik)

#sozluk ici sozluk tanımlanır fakat anahtar kısmına liste tanımlanamaz
kimlik = {
    "isim":"hakan",
    "Soyisim":"menguc",
    "yas":19,
    "yer":"duzce",
    "bilgiler":{"email":"askjasdja@gmail.com",
        "sosyalmedya":"@kaskljas",
    }
}
print(kimlik)

#sadece değerler kısmına liste tanımlana bilir
kimlik = {
    "isim":"hakan",
    "Soyisim":"menguc",
    "yas":19,
    "yer":["düzce","burundi"],
    "bilgiler":{"email":"askjasdja@gmail.com",
        "sosyalmedya":"@kaskljas",
    }
}
print(kimlik)