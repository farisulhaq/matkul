gaji_umr = 3000000
gaji = int(input("Masukkan gaji anda : "))
status = str(input('Apakah anda sudah menikah ? (sudah/belum) => '))
rmh = str(input('Apakah anda sudah memiliki rumah ? (sudah/belum) => '))
if gaji >= gaji_umr :
    if gaji > gaji_umr:
        print('Gaji anda sudah diatas UMR, maka anda wajib mengikuti asuransi')
    else:
        print('Gaji anda = UMR, maka anda tidak wajib mengikuti asuransi')
else :
    print('Gaji anda belum memenuhi UMR, maka anda tidak wajib mengikuti asuransi')
if status == 'sudah' :
    print('Anda sudah menikah, maka anda wajib menabung')
else :
    print('Anda belum menikah, maka anda tidak wajib menabung')
if rmh == 'belum' :
    print('Anda tidak memiliki rumah, maka anda tidak wajib membayar pajak rumah')
else : 
    print('Anda sudah memiliki rumah, maka anda wajib membayar pajak rumah')