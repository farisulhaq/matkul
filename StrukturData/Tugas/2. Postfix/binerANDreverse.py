# Ahmad Farisul Haq - 200411100171 #
# latihan 1 dan 2 modul stack pertemuan 2
# import stack
from stack import *
# fungsi reverse word dan conbert angka ke biner
def reverseORbiner(data):
    st = stack()
    temp = ''
    # cek type data 
    if type(data) == int:
        # untuk convert biner
        while data > 0:
            push(st,data % 2)
            data //= 2
    else:
        # untuk revert word
        for i in data:
            push(st,i)
    # dari stack di jadikan string di temp
    while not(isEmpty(st)):
        temp += str(pop(st))
    return temp
 
start = True
while start:
    print('1. Reverse Kata \n2. Konversi desimal ke biner \n3. Stop')
    inp = int(input('Pilih (1/2/3) : '))
    # untuk reverse word
    if inp == 1:
        word = input('Masukkan kata = ')
        reverse = reverseORbiner(word)
        print(word, 'menjadi', reverse)
    # untuk biner
    elif inp == 2:
        biner = int(input('masukkan angka = '))
        convert = reverseORbiner(biner)
        print("Biner dari {} adalah {}".format(biner,convert))
    # berhenti / lanjut
    else:
        start = False

