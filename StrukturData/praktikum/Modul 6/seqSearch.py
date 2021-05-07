# 200411100171 Ahmad Farisul Haq
def seqSearch(listData,data):
    temp = []
    ind = 0
    while ind < len(listData):
        if data == listData[ind]:
            temp.append(ind)
        ind += 1
    if temp == []:
        temp = "Data Tidak Ada"
    return temp,ind
# main Program
a = [1,5,9,8,1,5,10,26,5,12]
[hasil,jumlahIterasi] = seqSearch(a,5)
print("Posisi Data =",hasil)
print("Jumlah Iterasi =",jumlahIterasi)