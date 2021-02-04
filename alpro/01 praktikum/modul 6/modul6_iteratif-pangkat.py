# fungsi iterasi eksponensial
def expNumber(x,n):
    temp = 1
    for i in range(n):
        temp *= x
    return temp
# input user
x = int(input("masukkan angka = "))
n = int(input("masukkan pangkat = "))
# memanggil fungsi
pangkat = expNumber(x,n)
# cetak
print(x, "pangkat", n, "=", pangkat)
