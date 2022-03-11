print("Ahmad Farisul Haq")
'''
saya

'''
def queque():
    q = []
    return q
def enqueque(q,data):
    q.insert(0,data)
def dequeque(q):
    q.pop(0)
    return q


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
    que = queque()
    for i in data:
        enqueque(que,i)
    data = dequeque(que)
    temp = data
    i = 0
    while len(que) > 0:
        print("urutan ke -",i+1)
        print("nama pasien", temp[0])
        print("usia pasien", temp[1])
        if temp[1] >= 5 and temp[1] <= 15:
            wakt = 15
        elif temp[1] > 15 and temp[1] <= 30:
            wakt = 20
        else:
            wakt = 30
        sisa = temp[2] - wakt
        print("kegiatan konsul {} menit (sisa waktu {} menit)".format(wakt,sisa))
    
        temp[2] = sisa
        if sisa > 0:
            enqueque(temp)
        i += 1
    return que
print("pasien 1")
p1 = registrasi()
print("pasien 2")
p2 = registrasi()
p1 = [1,2,3]
p2 = [4,5,6]
a = sistem_antrian([p1,p2])
print(a)

        



