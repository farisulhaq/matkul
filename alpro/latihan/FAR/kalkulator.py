def tambah(a,b,c):
    if c == 1:
        hasil = a + b
    elif c == 2:
        hasil = a - b
    elif c == 3:
        hasil = a * b
    elif c == 4:
        hasil = a / b
    else:
        hasil = "perintah salah"
    return hasil

stop = False
while not(stop):
    x = int(input(" : "))
    start = True
    while start:
        y = int(input(" : "))
        z = int(input("(1/2/3/4)"))
        b = tambah(x,y,z)
        x = b
        print(b)
        i = input("ketik Y untuk lanjut nambah : ")
        if i.lower() == 't':
            start = False

