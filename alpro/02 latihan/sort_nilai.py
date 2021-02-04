a = [1,5,3,4,2]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            a[j],a[i] = a[i],a[j]
            
print(a)   
