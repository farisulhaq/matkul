la = []
genap = []
ganjil = []
prima = []
a = int(input("banyaknya bilangan : "))
for i in range(a):
    la.append(int(input("masukkan bilangan ke-"+str(i)+"= ")))
for i in la:
    if i % 2 == 0 and i not in genap:
        genap.append(i)  
    elif i%2 == 1 and i not in ganjil: 
        ganjil.append(i)
for i in la:
    if i > 1:
        for x in range(2,i):
            if i%x==0:
                break
        else:
            if i not in prima:
                prima.append(i)
print("bilangan =", la)
print("genap =", genap)
print("ganjil =", ganjil)
print("prima =", prima)