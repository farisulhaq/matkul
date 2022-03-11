# def merge_sort(arr,pilihan):
#     print("split",arr)
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         merge_sort(left,pilihan)
#         merge_sort(right,pilihan)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             out["perbandingan"] += 1
#             if pilihan == "a":
#                 if left[i] < right[j]:
#                     arr[k] = left[i]
#                     i += 1
#                 else:
#                     arr[k] = right[j]
#                     j += 1
#             else:
#                 if left[i] > right[j]:
#                     arr[k] = left[i]
#                     i += 1
#                 else:
#                     arr[k] = right[j]
#                     j += 1
#             k += 1
#             out["pergeseran"] += 1
#         while i < len(left):
#             out["pergeseran"] += 1
#             arr[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             out["pergeseran"] += 1
#             arr[k] = right[j]
#             j += 1
#             k += 1
#         print("merge",arr)

# def partition(arr,start,end,pilihan):
#     pivot = arr[end]
#     i = start
#     for j in range(start,end):
#         out["perbandingan"] += 1
#         if pilihan == "a":
#             if arr[j] < pivot:
#                 arr[j],arr[i]=arr[i],arr[j]
#                 i += 1
#         else:
#             if arr[j] > pivot:
#                 arr[j],arr[i]=arr[i],arr[j]
#                 i += 1
#         out["pergeseran"] += 1
#         print("proses",arr)
#     arr[i],arr[end]=arr[end],arr[i]
#     out["pergeseran"] += 1
#     print("proses",arr)
#     return i
# def quick_sort(arr,start,end,pilihan):
#     if start < end:
#         p = partition(arr,start,end,pilihan)
#         quick_sort(arr,start,p-1,pilihan)
#         quick_sort(arr,p+1,end,pilihan)

# start = True
# while start:
#     print(f"Sort Data\n1. Merge Sort\n2. Quick Sort")
#     pilih = int(input("Masukkan Pilihan (1/2) : "))
#     out = {"perbandingan":0,"pergeseran":0}
#     data = [5,1,6,2,4,3,9,0,-1]
#     if pilih == 1:
#         print(f"Sort Data\n1. Ascending\n2. Descanding")
#         jenis = int(input("Masukkan Pilihan (1/2) : "))
#         if jenis == 1:
#             merge_sort(data,"a")
#         else:
#             merge_sort(data,"d")
#         print(out)
#     elif pilih == 2:
#         print(f"Sort Data\n1. Ascending\n2. Descanding")
#         jenis = int(input("Masukkan Pilihan (1/2) :"))
#         if jenis == 1:
#             quick_sort(data,0,len(data)-1,"a")
#         else:
#             quick_sort(data,0,len(data)-1,"d")
#         print(out)
#     else:
#         start = False


def stack() :
    s = []
    return s
def push(s,data):
    s.append(data)
def pop(s):
    data = s.pop()
    return data
def peek(s) :
    data = s[len(s)-1]
    return (data)
def isEmpty(s) :
    return (s==[])
def size(s):
    return(len(s))

# fungsi pengecekan kurung
def cek_kurung(data):
    stk = stack()
    cek = True
    buka = '({['
    tutup = ')}]'
    for i in data :
        if i in buka :
            push(stk,i)
        elif i in tutup :
            if not(isEmpty(stk)) :
                if buka.index(peek(stk))==tutup.index(i) :
                    pop(stk)
                else :
                    return ('kurung buka dan tutup kurung tidak cocok')      
            else :
                return ('jumlah tutup kurung lebih banyak')
    if not(isEmpty(stk)) :
        return ('jumlah buka kurung lebih banyak')
    return (cek)

# fungsi operasi
def evaluasi (data) :
    oper = stack()
    operator = '+-/*'
    for i in data :
        if i not in operator : 
            push(oper,i)
        else :
            op1 = float(pop(oper))
            op2 = float(pop(oper))
            if i=='+' :
                hsl = op2 + op1
            elif i=='-' :
                hsl = op2 - op1
            elif i == '*' :
                hsl = op2 * op1
            else :
                hsl = op2 / op1
            push (oper,hsl)
    return (pop(oper))

def infixTopostfix(data) :
    if cek_kurung(data) is True:
        s = stack()
        operator = {'*':3,'/':3,'+':2,'-':2,'(':1,'[':1,'{':1}
        kurung = {')':'(','}':'{',']':'['}
        hasil = ""
        for i in data :
            if i.isnumeric() :
                hasil += i
            elif i in kurung.values() :
                push(s,i)
            elif i in kurung.keys() :
                temp = pop(s)
                while temp != kurung[i] :
                    hasil += temp
                    temp = pop(s)
            else :
                while not(isEmpty(s)) and operator[peek(s)] >= operator[i] :
                    hasil += pop(s)
                push(s,i)
        while not(isEmpty(s)) :
            hasil += pop(s)
        return True,hasil
    else :
        return False,cek_kurung(data)

start = True
while start :
    a = str(input('masukkan string operasi aritmatika = '))
    x,y = infixTopostfix(a)
    if x is True :
        print('infix : ',a,' ; ','postfix : ',y,' = ',evaluasi(y))
    else:
        print(y)
    if input("lagi ? y/t = ")=="t":
        start=False