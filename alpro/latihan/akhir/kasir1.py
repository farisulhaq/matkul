def display():
    print('Jumlah Harga =', sum(total_harga))
    jum_uang = int(input('Jumlah Uang : '))
    print('='*53*len(total_barang))
    print('barang yg dibeli', 'jumlah barang'.center(30), 'harga')
    for i in range(len(barang)):
        print(i+1, '.', barang[i], str(total_barang[i]).center(30), str(total_harga[i]).center(15))
    print('\n')
    print('Harga Total\t= ', ' '.center(14*2), sum(total_harga))
    print('uang anda\t= ', ' '.center(14*2), jum_uang)
    kembalian = jum_uang - sum(total_harga)
    print('kembalian anda\t=', ' '.center(14*2+1), kembalian)

def addMenu():
	print('tambah menu makanan')
	a = str(input('nama makanan : '))
	b = int(input('harga makanan : '))
	mak.append(a)
	makanan[a] = b
	
mak = ['','permen','coklat']
minu = ['','sprite','susu']
menu = ["pilih menu","makanan","minuman"]
makanan = {
	'permen' : 1000,
	'coklat' : 2000
}
minuman = {
	'sprite' : 3000,
	'susu' : 5000
}
barang = []
total_barang = []
total_harga = []
stop = False
print('selamat datang di aplikasi saya')
while not(stop):
	kode = input('masukkan kode : ')
	if kode == 'admin':
		addMenu()
	else:
		while not(stop):
			print((menu[0]).upper())
			for i in range(1,len(menu)):
				print(f'{i}. {menu[i]}')
			inp = int(input('silahkan masukkan pilihan : ' ))
			if inp == 1:
				no = 1
				for x in makanan:
					print(f'{no}. {x}')
					no += 1
				inp1 = int(input('masukkan pilihan (1/2)'))
				barang.append(mak[inp1])
			elif inp == 2:
				no = 1
				for x in minuman:
					print(f'{no}. {x}')
					no += 1
				inp1 = int(input('masukkan pilihan (1/2)'))
				barang.append(minu[inp1])
			inp2 = int(input('masukkan jumlah : '))
			total_barang.append(inp2)
			if mak[inp1] in makanan:
				total_harga.append(inp2*makanan[mak[inp1]])
			elif minu[inp1] in makanan:
				total_harga.append(inp2*minuman[minu[inp1]])
			input_ulang = input('tambah belanjaan?(y/t)')
			if input_ulang.lower() == "t":	
				display() 
				stop = True
		stop = True