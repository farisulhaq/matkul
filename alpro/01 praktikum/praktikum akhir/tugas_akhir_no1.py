# - Ahmad Farisul Haq - #
# - 200411100171      - #
# --- fungsi cek umr --- #
def soal1(nama,gaji,rumah,nikah):
    kalimat = ''
    if gaji >= 3000000:
        if gaji > 3000000:
            kalimat += 'Gaji %s diatas UMR, wajib untuk mengikuti asuransi, '%nama
        else:
            kalimat += 'Gaji %s pas UMR, tidak wajib untuk mengikuti asuransi, '%nama
    else:
        kalimat += 'Gaji %s dibawah UMR, tidak wajib mengikuti asuransi, '%nama
    if nikah == 1:
        kalimat += 'dan wajib menabung, '
    else:
        kalimat += 'dan tidak wajib menabung, '
    if rumah == 1:
        kalimat += 'serta wajib untuk membayar pajak '
    else:
        kalimat += 'serta tidak wajib untuk membayar pajak '
    return kalimat
# --- Main --- #   
nama = str(input('masukkan nama : '))
gaji = int(input('masukkan gaji (dalam angka) : '))
rumah = int(input("anda memiliki rumah? (jika iya ketik 1 / tidak ketik 2) : "))
nikah = int(input("sudah menikah ? (jika iya ketik 1 / tidak ketik 2) : "))
a = soal1(nama,gaji,rumah,nikah)
print(a)