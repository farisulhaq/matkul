nama_menu = ["nasi goreng","mie ayam"]
jumlah_barang = [2,10]
total_harga = [10000,9000]
print("="*101)
print("|","NO".center(4),"|","Nama Barang".center(25)+"|","jumlah".center(10),"|","Harga satuan".center(25),"|","Sub Total".center(24),"|")  
print("="*101)        
for i in range (len(nama_menu)) :
    print("|",str(i+1).center(4),"|",str(nama_menu[i]).center(25-3),"|",jumlah_barang[i],"|",total_harga[i]//jumlah_barang[i],"|",total_harga[i],"|")