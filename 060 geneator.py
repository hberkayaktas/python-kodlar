print("generatorler")

#bir say üretici (generator) tasarlayalım

def cift(sayı):
	cift_sayılar =[]
	for i in range(sayı):
		cift_sayılar.append(i*2)
	return cift_sayılar

print(cift(20))

#yukarıda bir fonksiyon tanımladık
#fonksiyonda return yerine yield kullanır isek 
#bir gnerator olur

def cift(sayı):
	for i in range(sayı):
		yield i*2
	
print(cift(20))

#yukarıdaki sorgu birsey çalıştırmaz çünkü 
#bir gnerator tanımladık

for i in cift(1000):
	print(i)

