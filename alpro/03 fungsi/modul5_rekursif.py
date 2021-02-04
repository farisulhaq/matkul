# fungsi rekursif eksponensial
def eksponensial(x,n):
    if n == 0:
        hasil = 1
    else:
        hasil = x * eksponensial(x,n-1)
    return hasil
# input user
x = int(input("masukkan angka : "))
n = int(input("masukkan pangkat : "))
# memanggil fungsi
pangkat = eksponensial(x,n)
# cetak
print(x, "pangkat", n, "=", pangkat)