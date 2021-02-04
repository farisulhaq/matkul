def creatlist(size):
    temp=[]
    for i in range(size):
        temp.append(int(input('masukkan data ke'+str(i)+'=')))
    return temp
def isprime(list):
    prime=[]
    for i in (list):
        if i>1:
            pembagi=0
            for o in range(2,i):
                if i%o==0:
                    pembagi+=1
            if pembagi==1 and i not in prime:
                prime.append(i)
    return prime
size=int(input('masukkan banyak data '))
list=creatlist(size)
prima=isprime(list)
print('list data',list)
print('prima',prima)