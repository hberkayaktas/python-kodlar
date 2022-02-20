import random
import time
import datetime
import sqlite3

con= sqlite3.connect("dersler.db")
cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS tablo1 (zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")

def rastgeledegerekle():
    zaman =time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-d %H:%M:%S'))
    anahtarkelime ="python sqllite"
    deger =random.randrange(0,10)
    cursor.execute("INSERT INTO tablo1 (zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()

def degerlerial():
    cursor.execute("SELECT * FROM Tablo1 WHERE deger = 2.0")
    data= cursor.fetchall()
    for i in data:
        print(i)
    con.commit()

def silveguncelle():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("ilk degerler ------------------------------------")
    for i in data:
        print(i)
    cursor.execute("UPDATE Tablo1 SET deger = 99 WHERE deger = 3")

    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Güncellendikten sonra ------------------------------------")
    for i in data:
        print(i)
    con.commit()

def silme():
    cursor.execute("DELETE FROM Tablo1  WHERE deger = 8")

    cursor.execute("SELECT * FROM Tablo1 WHERE deger = 8 ")
    data = cursor.fetchall()
    print("Güncellendikten sonra ------------------------------------")
    for i in data:
        print(i)
    con.commit()

def sadececagir():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("------------------------------------")
    for i in data:
        print(i)
    con.commit()

#tabloolustur()
"""""
i = 0

while (i <10):
    rastgeledegerekle()
    time.sleep(1)
    i+=1
"""
#degerlerial()
silveguncelle()

#silme()
#sadececagir()
con.close()
