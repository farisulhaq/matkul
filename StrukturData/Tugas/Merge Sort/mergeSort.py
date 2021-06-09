def merge_sort(arr,pilihan):
    print("split",arr)
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left,pilihan)
        merge_sort(right,pilihan)
        i = j = k = 0
        while i < len(left) and j < len(right):
            out["perbandingan"] += 1
            if pilihan == "a":
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
            else:
                if left[i] > right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
            k += 1
            out["pergeseran"] += 1
        while i < len(left):
            out["pergeseran"] += 1
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            out["pergeseran"] += 1
            arr[k] = right[j]
            j += 1
            k += 1
        print("merge",arr)

def partition(arr,start,end,pilihan):
    pivot = arr[end]
    i = start
    for j in range(start,end):
        out["perbandingan"] += 1
        if pilihan == "a":
            if arr[j] < pivot:
                arr[j],arr[i]=arr[i],arr[j]
                i += 1
        else:
            if arr[j] > pivot:
                arr[j],arr[i]=arr[i],arr[j]
                i += 1
        out["pergeseran"] += 1
        print("proses",arr)
    arr[i],arr[end]=arr[end],arr[i]
    out["pergeseran"] += 1
    print("proses",arr)
    return i
def quick_sort(arr,start,end,pilihan):
    if start < end:
        p = partition(arr,start,end,pilihan)
        quick_sort(arr,start,p-1,pilihan)
        quick_sort(arr,p+1,end,pilihan)

start = True
while start:
    print(f"Sort Data\n1. Merge Sort\n2. Quick Sort")
    pilih = int(input("Masukkan Pilihan (1/2) : "))
    out = {"perbandingan":0,"pergeseran":0}
    data = [5,1,6,2,4,3,9,0,-1]
    if pilih == 1:
        print(f"Sort Data\n1. Ascending\n2. Descanding")
        jenis = int(input("Masukkan Pilihan (1/2) : "))
        if jenis == 1:
            merge_sort(data,"a")
        else:
            merge_sort(data,"d")
        print(out)
    elif pilih == 2:
        print(f"Sort Data\n1. Ascending\n2. Descanding")
        jenis = int(input("Masukkan Pilihan (1/2) :"))
        if jenis == 1:
            quick_sort(data,0,len(data)-1,"a")
        else:
            quick_sort(data,0,len(data)-1,"d")
        print(out)
    else:
        start = False
