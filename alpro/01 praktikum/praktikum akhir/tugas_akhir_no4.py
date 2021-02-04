# - Ahmad Farisul Haq - #
# - 200411100171      - #
# --- fungsi search --- #
def soal4(kata):
    a = input('Masukkan Data Yg Mau Di Cari = ')
    temp = 0
    data = 0
    if a.lower() not in kata:
        print('Data Tidak Ditemukan')
    else:
        for i in kata:
            if a.lower() == i:
                print('Data %s ada di index ke - %d'%(a,temp))
                data += 1
            temp += 1
        print('\nJumlah data %s sebanyak = %d\n'%(a,data))
# --- Main --- #
a = ["if", "you","rerun", "the", "analysis", "using", "our", "algoritms", "and", "our", "data", "you", "will", "not", "get", "the", "identical", "result", "as", "provided", "here", "the",'reason','is','an','inherent','stochastic','component','in','these','result','all','test','are','based','on',"surrogates","surrogates","are","random","signal"]
print('Searching Data in list\n')
stop = False
while not(stop):
    soal4(a)
    inp = input('y untuk cari lagi = ')
    if inp.lower() == 't':
        stop = True




