sozluk = {"python":"güzel bir dil","php":"Script dili","java":"compile edilen dil"}

print(sozluk["python"])

for i in sozluk.items():
    print(i)

print("\n--------------------------------------------------------\n")
for i in sozluk.items():
    print(i[0] +" " + i[1])

print("\n--------------------------------------------------------\n")
for i,j in sozluk.items():
    print(i + " " + j)
    
print("\n--------------------------------------------------------\n")