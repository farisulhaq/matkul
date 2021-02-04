inp = int(input("masukkan jumlah mahasiswa : "))
nama = []
nilai = []
for i in range(1,inp+1):
    print("mahasiswa ke",i)
    nm = input("masukkan nama mahasiswa : ")
    nama.append(nm)
    nil = int(input("masukkan nilai mahasiswa : "))
    nilai.append(nil)
print("="*40)
stop = False
while not(stop):
    print("Data Nilai Mahasiswa")
    print("Tekan 0 untuk Daftar keseluruhan mahasiswa dan nilainya")
    print("Tekan 1 perhitungan rata-rata")
    print("Tekan 2 untuk  mahasiswa dengan nilai lebih dari threshold")
    print("Tekan 3 nilai tertinggi")
    input_1 = int(input("masukkan pilihan anda = "))
    if input_1 == 0:
        temp = 0
        for nama_nilai in range(len(nama)):
            temp += 1
            print(temp, ".", nama[nama_nilai], " : ",nilai[nama_nilai])
    elif input_1 == 1:
        juml = 0
        for rata in nilai:
            juml += rata
        print("rata-rata nilai =",juml/len(nilai))
    elif input_1 == 2:
        inp_user = int(input("masukkan angka : "))
        print("nilai yg lebih besar dari", inp_user, "adalah")
        temp = 0
        for bsr in nilai:
            if bsr > inp_user:
                print(nama[temp], " : ",nilai[temp])
            temp += 1
    elif input_1 == 3:
        maks = nilai[0]
        for i in range(len(nilai)):
            if maks < nilai[i]:
                maks = nilai[i]
        print(f'nilai tertinggi adalah {maks}')             
    clues = input("ingin mengulang operasi kembali (y/t) ? ")
    if clues == "t":
        stop = True
    print("="*50)
    