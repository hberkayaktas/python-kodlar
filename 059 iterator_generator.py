print("İterasyonlar")

x = 'mehmet'
for i in x:
	print(i)
	
y = [1,2,3,4,5,6]
for i in y:
	print(i)
	
#yukarıdaki x ve y değişkni gibi liste ve 
#string değişkenleri itere edilbilir değişkenler olarak
#geçen değişkenlerdir

#misal x değerini değiken atayalım ve manuel olarak itere edelim
iterasyon = iter(x)

print(next(iterasyon))
print(next(iterasyon))

#veyabir fonksiyon vasıtası ile itere edelim

while True:
	try:
		eleman = next(iterasyon)
		print(eleman)
	except StopIteration:
		break
		
#veya kendi iteratorlerimizi yazıp belli motorlar ile itere edebiliriz.
#bu motorlar __iter__() ve __next__() dir

class Sayılar:
	def __iter__(self):
		self.sayı= 0
		return self
		
	def __next__(self):
		x = self.sayı
		self.sayı +=5
		return x

bestaneartaniterasyon = Sayılar()
iterasyon = iter(bestaneartaniterasyon)

print(next(iterasyon))
print(next(iterasyon))