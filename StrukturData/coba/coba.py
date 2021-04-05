def binerKeDesimal(biner):
    desimal = 0
    for i in range(len(biner)):
        iDes = int(biner[i]) * (2**((len(biner)-1)-i))
        desimal += iDes
    return desimal
a = binerKeDesimal("1010")
print(a)

