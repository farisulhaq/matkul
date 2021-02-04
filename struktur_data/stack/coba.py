from stack import*

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
