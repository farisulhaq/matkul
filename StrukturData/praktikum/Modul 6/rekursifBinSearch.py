def binarySearch2(listData, data, awal, akhir, iterasi, listNol=[]):
    if awal > akhir:
        if listNol == []:
            return "Data Tidak Ada",iterasi
        else:
            return listNol,iterasi
    else:
        mid = (awal + akhir) // 2
        if listData[mid] == data:
            listNol.append(mid)
            if listData[mid + 1] == data:
                return binarySearch2(listData, data, mid+1, akhir, iterasi+1)
            elif listData[mid - 1] == data:
                return binarySearch2(listData, data,awal,mid-1, iterasi+1)
        else:
            if data < listData[mid]:
                return binarySearch2(listData, data,awal,mid-1, iterasi+1)
            else:
                return binarySearch2(listData, data,mid+1,akhir, iterasi+1)
a = [1,1,5,5,5,5,5,5,8,9,10,12,26,26]
first = 0
last = len(a)-1
[hasil,iterasi] = binarySearch2(a,0,first,last,0)
print("Posisi Data =",hasil)
print("Jumlah Iterasi =",iterasi)