import stack as st
def cek_kurung(data):
    stk = st.stack() # 
    cek = True
    buka = '({['
    tutup = ')}]'
    for i in data : #((1+2)
        if i in buka :
            st.push(stk,i)
        elif i in tutup :
            if not(st.isEmpty(stk)) :
                if buka.index(st.peek(stk))==tutup.index(i) :
                    st.pop(stk)
                else :
                    return ('kurung buka dan tutup kurung tidak sama')      
            else :
                return ('jumlah tutup kurung lebih banyak')
    if not(st.isEmpty(stk)) :
        return ('jumlah buka kurung lebih banyak')
    return (cek)
# fungsi operasi
def evaluasi (data) :
    oper = st.stack() #
    operator = '+-/*'
    for i in data : #12+2-
        if i not in operator :
            st.push(oper,i)
        else :
            op1 = float(st.pop(oper)) 
            op2 = float(st.pop(oper)) 
            if i=='+' :
                hsl = op2 + op1
            elif i=='-' :
                hsl = op2 - op1
            elif i == '*' :
                hsl = op2 * op1
            else :
                hsl = op2 / op1
            st.push (oper,hsl)
    return (st.pop(oper))

def infixTopostfix(data) : # (1+2
    if cek_kurung(data) is True:
        s = st.stack() #
        operator = {'*':3,'/':3,'+':2,'-':2,'(':1,'[':1,'{':1}
        buka = "({["
        tutup = ")}]"
        hasil = ""
        for i in data : #1+2*3
            if i.isnumeric() :
                hasil += i
            elif i in buka:
                st.push(s,i)
            elif i in tutup: 
                temp = st.pop(s)
                while temp != buka[tutup.index(i)] :
                    hasil += temp
                    temp = st.pop(s)
            else :
                while not(st.isEmpty(s)) and operator[st.peek(s)] >= operator[i] :
                    hasil += st.pop(s)
                st.push(s,i)
        while not(st.isEmpty(s)) :
            hasil += st.pop(s)
        return True, hasil
    else :
        return False, cek_kurung(data)
        
star = True
while star:
    a = input('masukkan string operasi aritmatika = ')
    x,y = infixTopostfix(a)
    if x is True:
        print('infix : ',a,' ; ','postfix : ',y,' = ',evaluasi(y))
    else:
        print(y)
    if input("lagi? ") == "n":
        star = False