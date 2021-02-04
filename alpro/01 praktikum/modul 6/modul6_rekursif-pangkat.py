# fungsi rekursif eksponensial
def expNumber(x,n):
    if n == 0:
        hasil = 1
    else:
        hasil = x * expNumber(x,n-1)
    return hasil
# input user
x = int(input("masukkan angka = "))
n = int(input("masukkan pangkat = "))
# memanggil fungsi
hasil = expNumber(x,n)
# cetak
print(x, "pangkat", n, "=", hasil)