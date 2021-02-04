# def menu_barang(a,b):
#     print('No.','Nama Cemilan\t','Harga')
#     for i in range(len(a)):
#         print(i+1,'.',a[i],'\t\t',b[i])

 

# menu = ['Beli Barang','Hapus Barang','Cetak Barang','Pembayaran']
# barang = ['','Cemilan','Minuman']
# cemilan = ['','Mie','Permen']
# harga_c = [5000,500]
# minuman = ['susu','aqua']
# harga_m = [2000,1000]
# stop = False
# while not(stop):
#     print('='*50)
#     print('Pilihan Menu')
#     for i in range(len(menu)):
#         print(f'{i+1}. {menu[i]}')
#     inp = int(input('Masukkan Pilihan Menu (1/2/3/4) : '))
#     if inp == 1:
#         for i in range(len(barang)):
#             print(f'{i+1}. {barang[i]}')
#         inp_barang = int(input('Masukkan Pilihan Menu (1/2) : '))
#         if inp_barang == 1:
#             menu_barang(cemilan,harga_c)
#             inp_pilih = int(input('Pilih Cemilan : '))
#             inp_juml = int(input('Masukkan Jumlah : '))
#         elif inp_barang == 2:
#             menu_barang(minuman,harga_m)
#     stop = True

makanan = {
	'permen' : 1000,
	'coklat' : 2000
}
if 1 == 1:
    no = 1
    for i in makanan:
        print(f'{no}. {i}')
        no += 1
    inp2 = int(input('masukkan jumlah : '))