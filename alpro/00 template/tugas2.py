a = int(input("masukkan suku awal :"))
b = int(input("masukkan beda :"))
d = int(input("Total : "))
temp = 0
sn = 0
n = 0
c = 0
while (sn + c) < d:
	temp += 1
	n = n + 1
	un = a + (n-1)*b
	c = un
	sn += un
	print("suku -", temp, "=", un, "total =", sn)
