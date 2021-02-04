# - Ahmad Farisul Haq - #
# - 200411100171      - #
# --- fungsi convert jam --- #
def soal2():
    jam = 0
    menit = 0
    detik = 0
    j = int(input('Masukkan Jam = '))
    if j < 24:
        jam += j
        m = int(input('Masukkan Menit = '))
        if m >= 60:
            jam += 1
            if jam == 24:
                jam -= 24
            menit += (m-60)
        else:
            menit += m
        d = int(input('Masukkan detik = '))
        if d >= 60:
            menit += 1
        else:
            detik += d
        print('Jam %s : %s : %s'%(str(jam).zfill(2),str(menit).zfill(2),str(detik).zfill(2)))
    else:
        print('jam tidak boleh lebih dari 23')
# --- Main --- #
print('---///program menginputkan angka ke dalam jam digital///---')
stop = False
while not(stop):
    soal2()
    a = input('Mau coba lagi (y/t) = ')
    if a.lower() == 't':
        stop = True
print('---///SELESAI///---')