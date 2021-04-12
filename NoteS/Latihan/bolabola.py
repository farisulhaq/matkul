def prima(angka):
    if angka <= 1:
        return False
    else:
        for i in range(2,angka):
            if angka % i == 0:
                return False
        return True

a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(2,a[1]+2):
    if not(prima(i)):
        b.append(i)
b.sort()
print(b)
print(b.index(a[1])+1)