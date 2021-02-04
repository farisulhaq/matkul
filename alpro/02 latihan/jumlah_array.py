a = [1,2,3,4,1]
b = [1,1,1,1]
jml = []
if len(a) == len(b):
    for i in range(len(a)):
        jml.append(a[i]+b[i])
    print(jml)
else:
    print("saya")
