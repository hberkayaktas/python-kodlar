import sqlite3
#pip install pysqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT,soyad TEXT,numara INT,ogrencinotu INT)")
    

def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('berkay','aktaş',1234,85)")
    con.commit()
    con.close()

tabloolustur()
degerekle()