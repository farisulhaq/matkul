def genapGanjil(data):
    if len(data) % 2 == 0:
        n = len(data)
    else:
        n = len(data) + 1
    print("Data =",data)
    for i in range(n//2):
        for j in range(0,len(data)-1,2):
            if data[j] > data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
        print("Genap-Ganjil Sorting\n{}".format(data))
        for y in range(1,len(data)-1,2):
            if data[y] > data[y+1]:
                data[y],data[y+1]=data[y+1],data[y]
        print("Ganjil-Genap Sorting\n{}".format(data))
    return data
a = [13,12,10,8,7,5,11,2,0]
b = genapGanjil(a)
print("Data Urut =",b)