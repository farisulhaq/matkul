print("Ahmad Farisul Haq")
'''
saya

'''
def queque():
    q = []
    return q
def enqueque(q,data):
    q.insert(0,data)
    return q
def dequeque(q):
    data = q.pop()
    return data
def isEmpty(q):
    return (q == [])
def size(q):
    return (len(q))


def registrasi():
    temp = []
    nama = input("Masukkan nama = ")
    temp.append(nama)
    usia = int(input("Usia pasien = "))
    temp.append(usia)
    waktu = int(input("Mau konsul berapa menit ?"))
    temp.append(waktu)
    return temp
    

def sistem_antrian(data):
    pasien = {}
    que = queque()
    total = 0
    for i in data:
        pasien[i[0]] = [i[1],i[2]]
        enqueque(que,i)
    i = 0
    while not(isEmpty(que)):
        obat = 10
        temp = dequeque(que)
        print("urutan ke -",i+1)
        print("Nama pasien =", temp[0])
        print("Usia pasien =", temp[1])
        if temp[1] >= 5 and temp[1] <= 15:
            wakt = 15
        elif temp[1] > 15 and temp[1] <= 30:
            wakt = 20
        else:
            wakt = 30
        sisa = temp[2] - wakt
        if sisa >= 0:
            print("Kegiatan = konsul {} menit (sisa waktu {} menit)".format(wakt,sisa))
            total += wakt
            temp[2] = sisa
            enqueque(que,temp)
        else:
            total += obat
            print("Kegiatan = beli obat {} menit (pasien meninggalkan klinik)".format(obat))
        waktu_total = "total waktu di klinik = {} menit".format(total)
        pasien[temp[0]][1] = waktu_total
        print(waktu_total)
        i += 1
    return pasien

def list_detail_antrian():
    print("pasien 1")
    p1 = registrasi()
    print("pasien 2")
    p2 = registrasi()
    a = sistem_antrian([p1,p2])
    print("="*20)
    x = 1
    for i in a:
        print("pasien",x)
        print("="*10)
        print("Nama =",i)
        print("Usia = {} tahun".format(a[i][0]))
        print(a[i][1])
        x += 1
    return
list_detail_antrian()





