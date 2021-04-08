import random
def bubble(data):
    ulang = {"kanan":0,"kiri":0}
    n = len(data)
    for i in range(len(data)//2):
        print("perulangan",i+1)
        temp = 0
        for x in range(i,n-1):
            if data[x] > data[x+1]:
                data[x],data[x+1]=data[x+1],data[x]
                temp += 1
                ulang["kanan"] += 1
            print(data)
        if temp == 0:
            break
        else:
            print("Putar Balik")
            for y in reversed(range(i+1,n-1)):
                if data[y] < data[y-1]:
                    data[y],data[y-1]=data[y-1],data[y]
                    ulang["kiri"] += 1
                print(data) 
        n -= 1
    print("kanan",ulang['kanan'])
    print("kiri", ulang["kiri"])
    return data
# data = random.sample(range(0,15),10)
data = [10,2,5,8,1,20,2,2,4]
bubble(data)