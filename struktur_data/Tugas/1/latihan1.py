# ahmad farisul haq 200411100171 #
#  latihan 1
start = True
while start == True:
    print('latihan 1 \n1. faktorial \n2. bilangan prima \n3. keluar')
    inp = int(input('pilih (1/2) : '))
    if inp == 1:
        print('bilangan faktorial')
        n = int(input('masukkan angka : '))
        temp = 1
        for i in range(2,n+1):
            temp *= i
        print("Hasil dari {}! adalah {}".format(n,temp))
    elif inp == 2:
        print('bilangan prima')
        angka = int(input('masukkan angka : '))
        if angka > 1:
            for num in range(2,angka):
                if angka % num == 0:
                    print(angka,'bukan bilangan prima')
                    break
            else:
                print(angka,'bilangan prima')
        else:
            print('bukan bilangan prima')
    else:
        start = False
