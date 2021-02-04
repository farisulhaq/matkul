def createlist(size):
    temp=[]
    for i in range(size):
        temp.append(int(input('masukkan data ke'+str(i)+'=')))
    return temp
def avglist(sise):
    jum = 0
    for i in sise:
        jum += i
    return jum/len(sise)
def addlist(c,d):
    if len(c)==len(d):
        jum = []
        for i in range(len(c)):
            jum.append(c[i]+d[i])
        return jum
    else:
        return "salah"
a = createlist(4)
print(a,";",avglist(a))
b = createlist(4)
print(b,";",avglist(b))
c = addlist(a,b)
d = addlist(c,c)
print(a,"+",b,"=",c)
print(c,"+",c,"=",d)
