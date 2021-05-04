# def angka(a):
#     print(float(angka))
#     return angka

# angka(1)
a = 7.1
print('$%0.2f'%a)

def square(n):
    return n*n
print(square(50))

def enough(cap, on, wait):
    return on - wait
print(enough(10,6j,5))



def b(x):
    hasil = 0
    for i in range(len(a)):
        w = 0
        if x[i] >= 10:
            w = 1
        else:
            w = 0
        hasil += (x[i] * w)/len(x)
    return hasil
a = [1,2,3,4,5,6,7,8,9,10]
print(b(a))



def bujur(x):
    mat = []
    if len(x) == len(bujur(x[1:])):
        for i in range(len(x)):
            hasil = x[i][i]
            mat.append(hasil)
        return mat
    else:
        return False
a = [[1,2,3],[4,5,6],[7,8,9]]
print(bujur(a))


def karakter(kata):
    krk = {}
    for i in kata.lower():
        krk[i] = krk.get(i,0) + 1
    return krk
def karakter1(kata):
    krk = {}
    for i in kata.lower():
        if i not in krk:
            krk[i] = 1
        else:
            krk[i] = krk[i] + 1
    return krk

kata = 'ALgoritma Pemrograman'
a = karakter(kata)
b = karakter1(kata)
print(a)
print(b)


def S(n):
    if len(n) == 1:
        hasil = a[0]
    else:
        hasil = n[-1] + S(n[:-1])
    return hasil
a = [1,3,5,7,9]
n = len(a)
S1 = a[0]
Un = a[-1]
Sn = S(a)
print('n =',n)
print('a =',S1)
print('Un =',Un)
print('Sn =',Sn)          
