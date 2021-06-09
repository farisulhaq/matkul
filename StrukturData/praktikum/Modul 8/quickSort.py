# def partition(arr,start,end):
#     pivot_index = start
#     pivot = arr[pivot_index]
#     while start < end:
#         while start < len(arr) and arr[start] >= pivot:
#             start += 1
#         while arr[end] < pivot:
#             end -= 1
#         if start < end:
#             arr[start], arr[end] = arr[end], arr[start]
#             print("proses",arr)
            
#     arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
#     print("proses",arr)
#     return end
# def quick_sort(arr,start,end):
#     if start < end:
#         p = partition(arr,start,end)
#         quick_sort(arr,start,p-1)
#         quick_sort(arr,p+1,end)
# data = [1,3,5,8,7,9,4,2,6]
# quick_sort(data,0,len(data)-1)

def partition(arr,start,end):
    pivot = arr[end]
    i = start
    for j in range(start,end):
        if arr[j] > pivot:
            arr[j],arr[i]=arr[i],arr[j]
            i += 1
    arr[i],arr[end]=arr[end],arr[i]
    print(arr)
    return i
def quick_sort(arr,start,end):
    if start < end:
        p = partition(arr,start,end)
        print(p)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)
data = [30,11,9,29,7,2,15,28]
quick_sort(data,0,len(data)-1)

