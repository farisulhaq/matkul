# 200411100171 Ahmad Farisul Haq
def binSearch(listData,data):
    first = 0
    last = len(listData) - 1
    temp = []
    found = False
    ind = 0
    while first <= last and not found:
        mid = (first + last) // 2
        if data == listData[mid]:
            temp.append(mid)
            if (mid + 1) == len(listData):
                found = True
            elif data == listData[mid + 1]:
                first = mid + 1
            elif data == listData[mid - 1]:
                last = mid - 1
            else:
                found = True
        else:
            if data <= listData[mid]:
                last = mid - 1
            else:
                first = mid + 1
        ind += 1
    if temp == []:
        temp = "Data Tidak Ada"
    return temp,ind
# main Program
def main(listData,data):
    mid = len(listData)//2
    if data == listData[mid]:
        x,y=binSearch(listData,data)
        
    if listData[mid-1] == data:
        a,b=binSearch(listData[:mid-1],data)
        print("q",a+x,b+y)
    else:
        i,j=binSearch(listData,data)
        print(i,j)
# main Program

a = [1,1,5,5,5,5,5,5,8,9,10,12,26,26,26,26,26]
main(a,26)
# [hasil,iterasi] = binSearch(a,5)
# print("Posisi Data =",hasil)
# print("Jumlah Iterasi =",iterasi)