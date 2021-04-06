from queque import *
# Fungsi membuat data dan Waktunya
def task(angka):
    que = createQueue()
    for i in range(angka):
        temp = [input(f'Nama Proses Ke-{i} : '),int(input('Waktu Proses : '))]
        enQueue(que,temp)
    return que
# Fungsi Penjadwalan
def queueProgram(data,waktu):
    print('Antrian Proses Beserta Waktunya =',data)
    num = 1
    while not(isEmpty(data)):
        print('Iterasi ke-',num)
        q = deQueue(data)
        if q[1] > waktu:
            q[1] -= waktu
            print(f'\tProses {q[0]} Sedang Diproses, Dan Sisa Waktu Proses {q[0]} = {q[1]}')
            enQueue(data,q)
        else:
            print(f'\tProses {q[0]} Telah Selesai Diproses')
        print('\tData Proses Yang Tersisa :',data)
        num += 1
# MAIN PROGRAM
num = int(input("Jumlah Proses Yang Akan Dijadwal  Di CPU = "))
data = task(num)
print(f"\nAntrian Proses :\n{data}\n")
wkt = int(input('Waktu Proses CPU = '))
queueProgram(data,wkt)

