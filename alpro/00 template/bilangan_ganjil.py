# Nama : Ahmad Farisul Haq
# Nim : 200411100171
num_ganjil = int(input("jumlah angka ganjil = "))
n = 0
for i in range(num_ganjil + num_ganjil):
    if i % 2 == 0:
        n += 1
        print("bilangan ganjil-",n, "=", i)
    