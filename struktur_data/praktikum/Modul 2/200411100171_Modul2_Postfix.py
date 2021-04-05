from stack import *
# fungsi cek kurung
def cekkurung(data):
    st = stack()
    kurung = {")":"(","}":"{","]":"["}
    for i in data:
        # cek i jika sama dengan "({["
        if i in kurung.values():
            push(st, i)
        # cek i jika sama dengan ")}]"
        elif i in kurung.keys():
            # cek st kosong atau tidak
            if not isEmpty(st):
                # jika nilai terakhir di stack = key dan value kurung sama maka akan di hapus
                if peek(st) == kurung[i]:
                    pop(st)
                # jika False
                else:
                    return ("Kurung Buka Dan Kurung Tutup Tidak Cocok")
            # jika False
            else:
                return ("Jumlah Kurung Tutup Lebih Banyak")
    # cek st kosong atau tidak
    if not isEmpty(st):
        return ("Jumlah Kurung Buka Lebih Banyak")
    return True
# fungsi konvert Postfix
def infixTOpostfix(data):
    # cek dari cekkurung apakah True 
    if cekkurung(data) is True:
        st = stack() # manggil fungsi stack
        operator = {"*":3,"/":3,"+":2,"-":2,"(":1,"{":1,"[":1} # operator mempunyai nilai
        kurung = {")":"(","}":"{","]":"["} # buka kurung pasangan
        output = "" # tempat penyimpanan
        for i in data: 
            if i.isnumeric(): # cek apakah niali i adalah angka
                output += i # disimpan ke output
            elif i in kurung.values(): # cek nilai i = value di dict kurung
                push(st, i) # memasukkan ke fungsi stack di varibel st
            elif i in kurung.keys(): # cek nilai i = key di dict kurung
                temp = pop(st) # menghapus nilai terakhir di fungsi stack dan di simpan ke temp
                while temp != kurung[i]: # akan di hapus nilai yang ada di dalam kurung
                    output += temp # dimasukkan ke output
                    temp = pop(st)
            else:
                while not isEmpty(st) and operator[peek(st)] >= operator[i]: # pengecekan perulangan 
                    output += pop(st) # dimasukkan ke output
                push(st, i) # memasukkan ke fungsi stack di varibel st
        while not isEmpty(st): # ngecek apakah masih ada nilai di fungsi stack v st
            output += pop(st) # dimasukkan ke output
        return True, output 
    else:
        return False, cekkurung(data)
# fungsi Evaluasi Postfix
def Evaluasi(data):
    st = stack() # fugsi stack
    output = ""
    for i in data:
        if i.isnumeric(): # cek i apakah angka
            push(st, i) # masukkan ke v st
        else:
            a = float(pop(st)) # hapus nilai terakhir
            b = float(pop(st)) # hapus nilai terakhir
            # pengecekan operator
            if i == "*":
                hasil = b * a
            elif i == "/":
                hasil = b / a
            elif i == "+":
                hasil = b + a
            elif i == "-":
                hasil = b - a
            push(st, hasil)
    while not isEmpty(st):
        output = str(pop(st)) + output
    return output
# main program #
stop = False
while not stop:
    inp = input('Masukkan String Operasi Aritmatika = ').replace(" ","")
    a,b = infixTOpostfix(inp)
    if a is True:
        print("infix: {} ; postfix: {} = {}".format(inp,b,Evaluasi(b)))
    else:
        print(b)
    if input('lagi? (y/n) : ').lower() == "n":
        print("-------")
        print("SELESAI")
        print("-------")
        stop = True