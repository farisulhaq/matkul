# fungsi stack
def stack():
    s = []
    return s
def push(s,data):
    s.append(data)
def pop(s):
    data = s.pop()
    return data
def peek(s):
    data = s[len(s)-1]
    return (data)
def isEmpty(s):
    return (s==[])
def size(s):
    return (len(s))
# fungsi cek kurung
def cekkurung(data):
    s = stack()
    kurung = {')':'(','}':'{',']':'['}
    pesan = True
    for i in data:
        if i in kurung.values():
            push(s,i)
        elif i in kurung.keys():
            if not(isEmpty(s)):
                if peek(s) == kurung[i]:
                    pop(s)
                else:
                    pesan = False
                    print('kurung buka dan kurung tutup tidak sama')
                    break
            else:
                pesan = False
                print('kelebihan tutup kurung')
                break
    if not(isEmpty(s)):
        pesan = False
        print('kelebihan buka kurung')
    return pesan