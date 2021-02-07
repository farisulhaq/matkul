from stack import *

def kalku(string):
    s = stack()
    ope = '+-/*'
    for i in string:
        if i in ope:
            if i == '-':
                if size(s) >= 2:
                    if peep(s) == ' ':
                        pop(s)
                    temp = pop(s)
                    if peep(s) == ' ':
                        pop(s)
                    push(s,pop(s)-temp)
                else:
                    return ('kekurangan operator')
            elif i == "+":
                if size(s) >= 2:
                    if peep(s) == ' ':
                        pop(s)
                    temp = pop(s)
                    if peep(s) == ' ':
                        pop(s)
                    push(s,pop(s)+temp)
                else:
                    return ('kekurangan operator')
            elif i == "/":
                if size(s) >= 2:
                    if peep(s) == ' ':
                        pop(s)
                        if peep(s) != 0:
                            temp = pop(s)
                        else:
                            return ('pembagian dengan nol')
                    if peep(s) == ' ':
                        pop(s)
                    push(s,pop(s)/temp)
                else:   
                    return ('kekurangan operator')             
        elif i == " ":
            push(s,i)
        else:
            push(s,int(i))
    if size(s) > 1:
        return ('kelebihan operator')
    else:
        return(pop(s))
a = kalku('1 2 + 6 - 2 /')
print(a)