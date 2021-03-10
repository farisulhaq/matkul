# Ahmad Farisul Haq - 200411100171 #
# latihan 3 modul stack pertemuan 2
# import stack
from stack import *
def postfix(data):
    # cek apakah buka kurung atau tutup kurung sesuai 
    if cekkurung(data):
        operator = {'*' : 3,'/' : 3,'+' : 2,'-' : 2,'(' : 1,'{':1,'[':1}
        kurung = {')':'(','}':'{',']':'['}
        st = stack()
        hasil = []
        # ubah string ke list 
        infix = data.split()
        for i in infix:
            # append buka kurung ke st 
            if i in '({[':
                push(st,i)
            # append angka atau huruf ke hasil
            elif i.isalnum():
                hasil.append(i)
            # append operator yg ada di dalam kurung
            elif i in ')}]':
                temp = pop(st)
                while temp != kurung[i]:
                    hasil.append(temp)
                    temp = pop(st)
            else:
                # pengecekan nilai operator
                while not(isEmpty(st)) and operator[peek(st)] >= operator[i]:
                    hasil.append(pop(st))
                push(st,i)
        # mengecek st masih ada nilai
        while not(isEmpty(st)):
            hasil.append(pop(st))
        # return sekaligus merubah list ke string
        return hasil
    else:
        return data
# main program
stop = False
while not(stop):
    infix = input('Masukkan aritmatika infix : ')
    # jika stop maka akan berhenti
    if infix == "stop":
        stop = True
    # else dari stop
    else:
        convert = postfix(infix)
        if type(convert) == list:
            print('Hasil Postfix = ', ' '.join(convert))
        else:
            print('kesalahan',convert)
