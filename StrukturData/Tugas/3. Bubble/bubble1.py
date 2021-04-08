def bubble(data):
    for i in reversed(range(len(data))):
        print("perulangan",i)
        x = 0
        for j in range(i):
            if data[j] > data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                x += 1
            print(data,x)
        if x == 0:
            break
a = [0,1,2,3,4,5,6]
bubble(a)