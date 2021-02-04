# def creatList(banyak):
#     temp=[]
#     for i in range(banyak):
#         temp.append(int(input('masukkan data ke '+str(i)+' = ')))
#     return temp
# def avgrange(banyak):
#     return sum(banyak)/len(banyak)
# def addList(list1,list2):
#     if len(list1)==len(list2):
#         penjumlahdata=[]
#         for i in list1:
#             penjumlahdata.append(list1[i]+list2[i])
#         return penjumlahdata
#     else:
#         return "salahh njir"
    
# data1 = creatList(6)
# print('data - 1',data1,': rata-rata list =', avgrange(data1))
# data2 = creatList(6)
# print('data - 1',data2,': rata-rata list =', avgrange(data2))
# hasil1 = addList(data1,data2)
# print(data1,' + ',data2,' = ',hasil1)
def creatList(banyak):
    temp=[]
    for i in range(banyak):
        temp.append(int(input('masukkan data ke '+str(i)+' = ')))
    return temp

def avgRange(bbanyak):
    temp=0
    for i in (bbanyak):
        temp+=i
    return temp/len(bbanyak)

def addList(a,b):
    penjumlahdata=[]
    if len(a)==len(b):
        for i in range(len(a)):
            penjumlahdata.append(a[i]+b[i])
        return penjumlahdata
    else:
        return 'panjang data tidak sama'
list1=creatList(4) 
print(list1,' : ',avgRange(list1))
list2=creatList(4)
print(list2,' ; ',avgRange(list2))
print(addList(list1,list2))