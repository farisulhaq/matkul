start = True
a = int(input("masukkan suku awal :"))
b = int(input("masukkan beda :"))
t_n = int(input("total :"))
sn = 0
while start:
    for n in range(1,t_n+1):
        sn += a
        while sn > t_n:
            start = False
        print("suku ke-", n, "=", a, "total =", sn)
        a = a+b
