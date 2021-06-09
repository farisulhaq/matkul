# AHMAD FARISUL HAQ
# 200411100171
def merge_sort(arr, pilihan):
    print("split =", arr)
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left, pilihan)
        merge_sort(right, pilihan)
        i = j = k = 0
        while i < len(left) and j < len(right):
            pesan["perbandingan"] += 1
            if pilihan == "a":
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            else:
                if left[i] > right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            pesan["pergeseran"] += 1

        while i < len(left):
            pesan["pergeseran"] += 1
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            pesan["pergeseran"] += 1
            arr[k] = right[j]
            j += 1
            k += 1
        print("merge =", arr)


def partition(arr, start, end, pilihan):
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
        if pilihan == "a":
            while start < len(arr) and arr[start] <= pivot:
                start += 1
            while arr[end] > pivot:
                end -= 1
        else:
            while start < len(arr) and arr[start] >= pivot:
                start += 1
            while arr[end] < pivot:
                end -= 1
        pesan["perbandingan"] += 1
        if start < end:
            pesan["pergeseran"] += 1
            arr[start], arr[end] = arr[end], arr[start]
            print("proses", arr)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    pesan["pergeseran"] += 1
    print("proses", arr)
    return end


def quick_sort(arr, start, end, pilihan):
    if start < end:
        p = partition(arr, start, end, pilihan)
        quick_sort(arr, start, p-1, pilihan)
        quick_sort(arr, p+1, end, pilihan)


# main Program
start = True
while start:
    print(f"Sort Data\n1. Merge Sort\n2. Quick Sort")
    pilih = int(input("Masukkan Pilihan (1/2) :"))
    pesan = {"perbandingan": 0, "pergeseran": 0}
    data = [1, 3, 5, 8, 7, 9, 4, 2, 6]
    if pilih == 1:
        print(f"Sort Data\n1. Ascending\n2. Descanding")
        jenis = int(input("Masukkan Pilihan (1/2) :"))
        if jenis == 1:
            merge_sort(data, "a")
        else:
            merge_sort(data, "d")
        print(pesan)
    elif pilih == 2:
        print(f"Sort Data\n1. Ascending\n2. Descanding")
        jenis = int(input("Masukkan Pilihan (1/2) :"))
        if jenis == 1:
            quick_sort(data, 0, len(data)-1, "a")
        else:
            quick_sort(data, 0, len(data)-1, "d")
        print(pesan)
    else:
        start = False
