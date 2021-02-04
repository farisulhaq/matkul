# # eksponen rekursif
# def eksponen(x,n):
#     if n == 0:
#         hasil = 1
#     else:
#         hasil = x + eksponen(x,n-1)
#     return hasil
# print(eksponen(9,5))
# # eksponen iteratif
# def pangkat(x,n):
#     temp = 1
#     for i in range(n):
#         temp *= x
#     return temp
# print(pangkat(9,5))
# def febi(x,n):
#     i = 0
#     temp = 1
#     while i < n:
#         temp *= x
#         i += 1
#     return temp
# print(febi(3,1))

def aritmatika(a,b,n):
    if n == 1:
        hasil = a
    else:
        hasil = b + aritmatika(a,b,n-1)
    return hasil
print(aritmatika(1,2,5))
