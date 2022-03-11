def insertion_sort(data):
    for i in range(1,len(data)):
        print(data)
        key = data[i]
        ind = i
        while ind > 0 and data[ind-1] >= key:
            data[ind] = data[ind-1]
            print("insert", data)
            ind -= 1
        data[ind] = key
    return data
        
# main data
import random
a = [8,5,2,3,4]
a = random.sample(range(1,20),10)
b = insertion_sort(a)
print(b)