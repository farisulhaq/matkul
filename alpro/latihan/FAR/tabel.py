a = [0]
header = ['NIM','NAMA','ALAMAT','KELAS']
x = [
    [200411100171,"a","sumenep","ALPRO A"],
    [200411100170,"b","pamekasan","ALPRO B"],
    [200411100169,"c","sampang","ALPRO C"]
]
def tabel (x) :
    print("-"*((16*5)-4))
    print("|"," "*2,'NO'," "*3,end="|")
    for baris in range (len(header)) :
        print(str(header[baris]).center(15),end="|")
    print()
    for kolom in range (len(x)) :
        print("-"*((16*5)-4))
        print("|"," "*3,a[-1]+1," "*3,end="|")
        a.append(a[-1]+1)
        for baris in range (len(x[kolom])) :
            print(str(x[kolom][baris]).center(15),end="|")
        print()
    print("-"*((16*5)-4))
tabel(x)
        
start = True 
while start :
    print("")
    print ("pilih menu mengatur data : ")
    print ("1.menambah data","\n2.menghapus data","\n3.urutkan data","\n4.cari mahasiswa dari Nim")
    pilihan = int(input("pilih menu :"))
    a.clear()
    a.append(0)
    if pilihan == 1 :
        temp = []
        temp.append(input("NIM : "))
        temp.append(input("NAMA : "))
        temp.append(input("ALAMAT : "))
        temp.append(input("KELAS : "))
        x.append(temp)
        tabel(x)
    elif pilihan == 2 :
        e = int(input("pilih nomor data : "))
        x.pop(e-1)
        tabel(x)
    elif pilihan == 3 :
        for i in range(len(x)):
            for j in range(i,len(x)):
                if x[i][0] > x[j][0]:
                    x[j],x[i] = x[i],x[j]
        tabel(x)
    elif pilihan == 4:
        y = []
        print('1. cari berdasarkan Nama\n2. cari berdasarkan Nim')
        pil = int(input("pilih menu (1/2) :"))
        if pil == 1:
            inp = input('Masukkan Nama yg akan di cari : ')
            for i in range(len(x)):
                if x[i][1] == inp:
                    y.append(x[i])
        elif pil == 2:
            inp = int(input('Masukkan Nim yg akan di cari : '))
            for i in range(len(x)):
                if x[i][0] == inp:
                    y.append(x[i])
        else:
            print('inputan salah/tidak sesuai')
            continue
        tabel(y)
    else :
        print("pilihan anda tidak ada di menu data","\nharap coba lagi")
