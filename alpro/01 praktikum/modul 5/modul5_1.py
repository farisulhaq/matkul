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
    prima = True
    for i in range(2,bilangan):
        if bilangan % i == 0:
            prima = False
    return prima
# input banyak bilangan di list data
inp = int(input("banyaknya bilangan = "))
data = createList(inp)
# peyimpan bilangan genap, ganjil, dan prima
genap = []
ganjil = []
prima = []
for i in range(len(data)):
    if isGenap(data[i]) and data[i] not in genap:
        genap.append(data[i])
    else:
        if not isGenap(data[i]) and data[i] not in ganjil:
            ganjil.append(data[i])
    if isPrime(data[i]) and data[i] not in prima and data[i] > 1:
        prima.append(data[i])
# cetak
print("bilangan =", data)
print("genap =", genap)
print("ganjil =", ganjil)
print("prima =", prima)