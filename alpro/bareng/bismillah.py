
def makanan () :
    print ('Pilihan Makanan :\n1. Bakso\n2. Mie Ayam\n3. Sate Ayam')
    mak = str(input('Masukkan Makanan yang dipilih : '))
    jumlah = int(input('Masukkan Jumlah : '))
    barang.append(mak)
    total_barang.append(jumlah)
    if mak.lower() == 'bakso' :
        harga = 7000 * jumlah
    elif mak.lower() == 'mie ayam' :
        harga = 7000 * jumlah
    elif mak.lower() == 'sate ayam' :
        harga = 10000* jumlah
    total_harga.append(harga)

def minuman () :
    print ('Pilihan Minuman :\n1. Es Teh\n2. Kopi\n3. Susu')
    min = str(input('Masukkan Minuman yang dipilih : '))
    banyak = int(input('Masukkan Jumlah : '))
    barang.append(min)
    total_barang.append(banyak)
    if min.lower() == 'es teh' :
        total = 2000 * banyak
    elif min.lower() == 'kopi':
        total = 4000 * banyak
    elif min.lower() == 'susu' :
        total = 5000 * banyak
    total_harga.append(total)

def camilan () :
    print ('Pilihan Camilan :\n1. Siomay\n2. Tahu Crispy\n3. Jamur Crispy')
    cam = str(input('Masukkan Camilan yang dipilih : '))
    jum = int(input('Masukkan Jumlah : '))
    barang.append(cam)
    total_barang.append(jum)
    if cam.lower() == 'siomay' :
        harg = 3000 * jum
    elif cam.lower() == 'tahu crispy' :
        harg = 2500 * jum
    elif cam.lower() == 'jamur crispy' :
        harg = 4000 * jum
    total_harga.append(harg)

def display():
    print('Jumlah Harga =', sum(total_harga))
    jum_uang = int(input('Jumlah Uang : '))
    print('='*53*len(total_barang))
    print('barang yg dibeli', 'jumlah barang'.center(30), 'harga')
    for i in range(len(barang)):
        print(i+1,'.', barang[i],' '*(19-len(barang[i])), str(total_barang[i]),' '*(21-len(str(total_barang[i]))), str(total_harga[i]))
    print('\n')
    print('Harga Total\t= ', ' '.center(14*2), sum(total_harga))
    print('uang anda\t= ', ' '.center(14*2), jum_uang)
    kembalian = jum_uang - sum(total_harga)
    print('kembalian anda\t=', ' '.center(14*2+1), kembalian)

barang = []
total_barang = []
total_harga = []

print ('='*100)
print ('|',' '*30,'SELAMAT DATANG DI WARUNG MURAHSAE',' '*(31),'|')
print ('='*100)
start = True
while start :
    print ('PILIHAN MENU\n1. Makanan\n2. Minuman\n3. Camilan'.upper())
    b = str(input('Masukkan Pilihan Menu : '.upper()))
    if b.lower() == 'makanan' :
        makanan ()
    elif b.lower() == 'minuman' :
        minuman ()
    elif b.lower() == 'camilan' :
        camilan ()
    c = str(input('Apakah ada tambahan pesanan (y/t) : '))
    if c.lower() == 't' :
        display()
        start = False