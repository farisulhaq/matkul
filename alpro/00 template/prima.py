print("untuk menentukan bilangan prima atau bukan")
ap = int(input("masukkan angka : "))
if ap > 1:
    for i in range(2,ap):
        if ap%i == 0:
            print(ap, "adalah bukan bilangan prima")
            break
    else:
        print(ap, "adalah bilangan prima")
else:
    print(ap, "adalah bukan bilangan prima")