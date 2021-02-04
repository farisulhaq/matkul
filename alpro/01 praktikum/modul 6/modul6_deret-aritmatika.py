# fungsi deret aritmatika
def deret(a,b,n):
	if n == 1:
		hasil = a
	else:
		hasil = b + deret(a,b,n-1)
	return hasil
# input user
a = int(input("masukkan suku awal = "))
b = int(input("beda beda = "))
n = int(input("masukkan banyaknya suku = "))
hasil = deret(a,b,n)
print("suku ke-", n, "=", hasil)