from stack import *

def db(angka):
    st = stack()
    temp = ''
    while angka > 0:
        push(st,angka % 2)
        angka = angka // 2
    while not(isEmpty(st)):
        temp += str(pop(st))
    return temp
a = db(10)
print(a)

# def addList(a,b):
#     if len(a) < len(b):
#         n = len(a)
#         jml = b.copy()
#     else:
#         n = len(b)
#         jml = a.copy()
#     for i in range(n):
#         jml[i] = a[i] + b[i]
#     return jml

# x = [2,1,5,6]
# y = [6,7]
# z = [3,7,9,0,2,4,6,2]
# print(addList(x,y))
# print(addList(x,z))