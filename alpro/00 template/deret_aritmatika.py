# Nama : Ahmad Farisul Haq
# Nim : 200411100171
print("Mencari jumlah suku ke-n")
a = int(input("Masukkan suku awal : "))
b = int(input("Masukkan beda : "))
c = int(input("Masukkan suku ke-n : "))
n, un = 0, 0
for i in range(c): 
    n = i + 1
    # rumus un = a + (n - 1)*b
    un = a + (n - 1)*b
    print("un",n,"=", un)
# rumus Sn = n/2 * (a + Un)
sn = (n / 2) * (a + un)
print("jumlah suku ke-1 sampai ke-",n,"=", sn)