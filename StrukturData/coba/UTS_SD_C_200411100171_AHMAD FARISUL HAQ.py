def GenapGanjil(data):
    print("data =",data)
    for i in range(len(data)//2):
        for j in range(0,len(data)-1,2):
            if data[j] > data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
        print("genap-ganjil",data)
        for y in range(1,len(data)-1,2):
            if data[y] > data[y+1]:
                data[y],data[y+1]=data[y+1],data[y]
        print("ganjil-genap",data)
    return data
data = [15,12,6,7,9,19,78,10,0,1,100,98]
cek = GenapGanjil(data)
print("urut =",cek)