#1
def sumNumber(a,b):
    c=a+b
    print(c)
    return c
num1=int(input('bilangan 1='))
num2=int(input('bilangan 2='))
c=sumNumber(num1,num2)
hasil=c*5
print(hasil)

# print()
# #2
# def setPassword():
#     password='tanggalLahirku'
#     return password
# def displayPassword(password):
#     print('the password is',password)

# passWd=setPassword()
# displayPassword(passWd)

# print()
#3
password='tanggalLahirku'
def setPassword3():
    password='namaku'
    # return password
def displayPassword3():
    print('the password is',password)
    
print(setPassword3())
displayPassword3()
