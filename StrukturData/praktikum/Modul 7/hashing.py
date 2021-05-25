def remainderFunction(data,num):
    return (data%num)

def createHashTable(num):
    temp = [['none']]*num
    return temp

def chaining(data,table):
    for i in data:
        slot = remainderFunction(i,len(table))
        if table[slot] == ['none']:
            table[slot] = [i]
        else:
            table[slot].append(i)
    return table
    
def searchHash(data,table):
    slot = remainderFunction(data,len(table))
    cek = 0
    for ind,num in enumerate(table[slot]):
        if num == data:
            print(f'(data berada di slot ke- {slot} dan indeks ke- {ind})')
            cek += 1
    if cek == 0:
        print(False)

print("remainder")
slot = remainderFunction(55,10)
print(slot)
print("creatHashTable")
hashTable = createHashTable(11)
print(hashTable)
print("chaining")
a = [54,26,93,17,77,31,44,55,20]
chaining(a,hashTable)
print(hashTable)
print("searchHash")
searchHash(66,hashTable)
searchHash(54,hashTable)
searchHash(20,hashTable)
searchHash(55,hashTable)
searchHash(100,hashTable)