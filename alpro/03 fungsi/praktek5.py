# fungsi input
def createList(jumlah):
    bil = []
    for i in range(jumlah):
        bil.append(int(input("masukkan bilangan ke - "+str(i)+"= ")))
    return bil
# fungsi genap
def isGenap(bilangan):
    return bilangan%2==0
# fungsi prima
def isPrime(bilangan):
    if bilangan > 1:
        for x in range(2,bilangan):
            if bilangan%x==0:
                return False
        else:
            return True
    else:
        return False
# input banyak bilangan di list data
inp = int(input("banyaknya bilangan = "))
data = createList(inp)
# peyimpan bilangan genap, ganjil, dan prima
genap = []
ganjil = []
prima = []
# append genap
for i in range(len(data)):
    if isGenap(data[i]) and data[i] not in genap:
        genap.append(data[i])
# append ganjil
for i in range(len(data)):
    if not isGenap(data[i]) and data[i] not in ganjil:
        ganjil.append(data[i])
# append prima
for i in range(len(data)):
    if isPrime(data[i]) and data[i] not in prima:
        prima.append(data[i])
# cetak
print("bilangan=", data)
print("genap=", genap)
print("ganjil=", ganjil)
print("prima=", prima)