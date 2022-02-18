#tek atırlı lambda fonksiyonu

def kare(x):
    return x**2

print(kare(8)) 
#fonksiyonları uzun uzun tanımlayabildiğimiz gibi
# aşağıdaki gibi tek satırda belli bir değişkene
# atıp sonradan çağıra biliriz 


x = lambda x:x**2
print(x(10))

x = [1,2,3,4,5,6,7,8,9,10]

y = list(filter(lambda x:(x%2==0), x))
#filtreleme fonksiyonu fonksiyonu filtreler 
# 2 ye bölümünden kalan 0 olan çıktılar gösterilir
#
print(y)

z = list(map(lambda x:x**2, x))
print(z)
#map fonksiyonu x listesi içinde her elemanın ayrı ayrı
#ele alır ve karesi olur
#
