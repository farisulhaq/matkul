from stack import *
def kurung(string):
    s = stack()
    cek = True
    pesan = 'tidak ada eror'
    for i in string:
        if i == '(' or i == '{':
            push(s,i)
        elif i == ')' and not(isEmpty(s)) and peep(s) == '(':
            pop(s)
        elif i == ')' or i == '}' and isEmpty(s):
            pesan = 'kelebihan tutup kurung'
        elif i == '}' and not(isEmpty(s)) and peep(s) == '{':
            pop(s)
    print(s)
    if size(s)>=1:
        cek = False
    return cek,pesan
a = kurung('())')
print(a)
