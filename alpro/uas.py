# def jumlah(a,b):
#     return a + b
# def kurang(a,b):
#     return a - b
# def kali(a,b):
#     return a * b
# def bagi(a,b):
#     return a / b
# def display(x):
#     print('hasil = %5d'%x)

# start = True
# while start:
#     print('1. penjumlahn\n2. pengurangan\n3. perkalian\n4. pembagian')
#     inp = int(input('masukkan (1/2/3/4) '))
#     a = int(input('masukkan angka 1 : '))
#     b = int(input('masukkan angka 2 : '))
#     if inp == 1:
#         x = jumlah(a,b)
#     elif inp == 2:
#         x = kurang(a,b)
#     elif inp == 3:
#         x = kali(a,b)
#     elif inp == 4:
#         x = bagi(a,b)
#     display(x)
#     inp1 = input('ulangi (y/t): ')
#     if inp1 == 't':
#         start = False

a = []
for i in range(4):
    b = []
    for j in range(4):
        if i == j or i < j:
            b.append(1)
        else:
            b.append(0)
    a.append(b)
for i in range(len(a)):
    print("|",end="")
    for j in range(len(a[0])):
        print("%4d"%(a[i][j]),end="")
    print("%4s"%"|")
