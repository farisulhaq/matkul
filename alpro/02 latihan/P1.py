angka = [1,2,3,4,5,6,7,8,9]
stop = False
while not(stop):
    temp = 0
    ank = ' '
    for i in angka:
        if i%2==1:
            print(i)
            temp += 1

    angka = [1,2,3,4,5,6,7,8,9]
    max = angka[0]
    for i in range(1,len(angka)):
        if max < angka[i]:
            max = angka[i]
    print("nilai mak = ",max)
    angka = [1,2,3,4,5,6,7,8,9]
    inp = int(input("masukkan angka = "))
    for i in angka:
        if inp < i:
            print("angka yang lebih besar dari %s adalah" % inp , i)
    retry = input("ingin mengulanginya (y/t) : ")
    if retry == "t":
        stop = True