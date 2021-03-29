menu = ['Beli Barang','Pembayaran']#'Hapus barang','Cek keranjang','Pembayaran']
cemilan = [['Mie',5000],['Permen',500]]
start = True
barang = []
while start:
    print('Pilihan Menu')
    for i in range(len(menu)):
        print(str(i+1)+".",menu[i])
    inp = int(input('Masukkan pilihan menu (1/2) : '))
    if inp == 1:
        print('1. Cemilan')
        ab = []
        in_me = int(input('Masukkan pilihan (1/2) : '))
        if in_me == 1:
            print('No',' ','Nama cemilan',' '*10,'Harga')
            for x in range(len(cemilan)):
                print(x+1,end=' '*4)
                for y in range(len(cemilan[x])):
                    print(cemilan[x][y],'\t',end=' '*13)
                print()
            a = int(input('Pilih camilan : '))
            b = cemilan[a-1][0]
            c = cemilan[a-1][1]
            juml = int(input('Masukkan jumlah : '))
            ab.append(b)
            ab.append(juml)
            ab.append(c*juml)
            barang.append(ab)
    else:
        print('No',' ','Nama cemilan',' '*10,'jumlah',' '*8,'Harga')
        for x in range(len(barang)):
            print(x+1,end=' '*4)
            for y in range(3):
                print(barang[x][y],'\t',end=' '*13)
            print()
        a = 0
        for i in range(len(barang)):
            a += barang[i][2]
        print('Total Harga = %d'%(a))


