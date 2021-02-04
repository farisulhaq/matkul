# - Ahmad Farisul Haq - #
# - 200411100171      - #
# --- fungsi triangularNumbers --- #
def triangularNumbers(a):
    if a == 1:
        hasil = 1
    else:
        hasil = a + triangularNumbers(a-1)
    return hasil
# --- Main --- #
b = int(input('masukkan angka : '))
jumlah = triangularNumbers(b)
print('Hasil dari triangularNumbers =',jumlah)
