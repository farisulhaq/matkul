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
        elif (i == '}' or i == ')') and (isEmpty(s)):
            pesan = 'kelebihan tutup kurung'
        elif i == '}' and not(isEmpty(s)) and peep(s) == '{':
            pop(s)
        elif ((i == ')') and (peep(s) == '{')) or ((i == '}') and (peep(s) == '(')):
            pesan = 'kurung buka dan kurung tutup tidak sama'
            pop(s)
    if not(isEmpty(s)):
        cek = False
        pesan = 'kelebihan kurung buka'
    elif pesan != 'tidak ada eror':
        cek = False
    return cek, pesan
a = kurung('(}')
print(a)
