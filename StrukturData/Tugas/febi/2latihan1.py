from stack import *
def cek_kurung(data):
    s = stack()
    cek = True
    for i in data:
        if i == '(':
            push(s,i)
        elif i == ')' and not(isEmpty(s)) and peek(s) == '(':
            pop(s)
        elif i == ')' and isEmpty(s):
            cek = False
            print('kelebihan tutup kurung')
    while not(isEmpty(s)):
        pop(s)
        cek = False 
        print('kelebihan kurung buka')
    return cek

def InfixtoPostfix(data):
    if cek_kurung(data):
        operator = {'*':2,'/':2,'+':1,'-':1,'(':0}
        st = stack()
        output = []
        febi = data.split()
        angka = '0123456789'
        for i in febi:
            if i in angka:
                output.append(i)
            elif i == '(':
                push(st,i)
            elif i == ')':
                temp = pop(st)
                while temp != '(':
                    output.append(temp)
                    temp = pop(st)
            else:
                while not(isEmpty(st)) and operator[peek(st)] >= operator[i]:
                    output.append(pop(st))
                push(st,i)
        while not(isEmpty(st)):
            output.append(pop(st))
        return " ".join(output)
    return data

data = '4 * 4 + 4'
a = InfixtoPostfix(data)
print(a)

