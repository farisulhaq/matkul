# a = [1,2,3,4,5]
# b = [1,2,3]
# c = []
# for i,j in zip(b,c):
#     c.append(i+j)
# print(c)
# genap = []
# ganjil = []
# la = [1,2,3,3,4,4,5]
# for i in la:
#     if i % 2 == 0:
#         genap.append(i) 
#     else:
#         ganjil.append(i)
stop = False
a = []
while not(stop):
    b = str(input("masukkan data : "))
    if b not in a:
        a.append(b)
    else:
        print("duplikasi")
        print(f'data {b} di index {a.index(b)}')
        print(f'data {b} sudah terhapus')
    c = input("input y : ")
    if c == "y":
        stop = False
    else:
        print("my list = ",a)
        stop = True
