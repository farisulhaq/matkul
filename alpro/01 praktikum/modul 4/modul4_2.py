la = []
lb = []
jml = []
a = int(input("banyaknya elemen matriks-1 = "))
for i in range(a):
    la.append(int(input("masukkan bilangan ke-"+str(i)+"= ")))
b = int(input("banyaknya elemen matriks-2 = "))
for i in range(b):
    lb.append(int(input("masukkan bilangan ke-"+str(i)+"= ")))
print("matriks 1 =", la)
print("matriks 2 =", lb)
if a == b:
    n = a
    jml = la.copy()
    for i in range(a):
        jml[i] = la[i]+lb[i]
    print("matriks 1 + matriks 2 =", jml)
else:
    print("ukuran matriks tidak sama")

