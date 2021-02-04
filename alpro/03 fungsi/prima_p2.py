def li(b):
    data = []
    for i in range(b):
        inp = int(input("masukkan data"+str(i)+":"))
        data.append(inp)
    return data
def data(a):
    prima = []
    for i in a:
        if i>1:
            for x in range(2,i):
                if i%x==0:
                    break
            else:
                if i not in prima:
                    prima.append(i)
    return prima
aku = li(5)
print(aku)
saya = data(aku)
print(saya)