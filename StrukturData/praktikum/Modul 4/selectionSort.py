def selectionSort(data):
    n = len(data)
    print(data)
    for i in range(len(data)//2):
        print("Iterasi ke-",i+1)
        ind = i
        for j in range(i+1,n):
            if data[ind] > data[j]:
                ind = j
        data[i],data[ind]=data[ind],data[i]
        print("urutan data minimal :",data)
        ind = n - 1
        for y in reversed(range(i+1,n-1)):
            if data[ind] < data[y]:
                ind = y
        data[n-1],data[ind]=data[ind],data[n-1]
        print("urutan data maksimal :",data)
        n -= 1
    return data
a = [12,5,8,1,20,7,12,4,0,1,0]
b = selectionSort(a)
print("Data urut =",b)