from stack import *
# # biner #
# def dec2bin(num) :
#     st = stack() #selalu diawali dengan great stack itu sendiri
#     divNum = num
#     while divNum > 0 :
#         push(st,divNum%2)
#         divNum = divNum//2
#     temp = ""
#     while not(isEmpty(st)) :
#         temp = temp + str(pop(st))
#     return temp
# print(dec2bin(10))

# # balik #
# def balik(a):
#     s = stack()
#     for i in a:
#         push(s,i)
#     temp = ''
#     while not(isEmpty(s)):
#         temp += pop(s)
#     return temp
# a = 'zahra'
# b = balik(a)
# print(b)

def matematika(string):
    s = stack()
    's = [(]'
    eror = 'benar'
    for i in string:
        if i == '(' or i == '{':
            push(s,i)
        elif i == ')' and not(isEmpty(s)) and peep(s) == '(':
            pop(s)
        elif i == ')' and isEmpty(s):
            eror = 'kekurangan tutup kurung'
        
    print(s)
    if size(s) >= 1:
        eror = "kelebihan buka kurung"
    return eror

a = '(()'
print(matematika(a))
