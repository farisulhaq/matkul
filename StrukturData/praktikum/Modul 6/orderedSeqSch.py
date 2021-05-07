# 200411100171 Ahmad Farisul Haq
def orderedSeqSch(listData,data):
    temp = []
    found = False
    ind = 0
    while ind < len(listData) and not found:
        if data == listData[ind]:
            temp.append(ind)
        elif data < listData[ind]:
            found = True
        ind += 1
    if temp == []:
        temp = "Data Tidak Ada"
    return temp,ind
# main Program
a = [1,1,5,5,5,8,9,10,12,26]
[hasil,iterasi] = orderedSeqSch(a,5)
print("Posisi Data =",hasil)
print("Jumlah Iterasi =",iterasi)