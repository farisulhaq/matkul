def pembagi(bilangan):
    faktor =[]
    for i in range(1,bilangan+1):
        if bilangan%i==0:
            faktor.append(i)
    return faktor
inp = int(input("masukkan angka = "))
bagi = pembagi(inp)
print("bilangan pembagi = ",bagi)