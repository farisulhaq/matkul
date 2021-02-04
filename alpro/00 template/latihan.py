'''
lower = int(input("batas bawah :"))
upper = int(input("batas atas :"))
for num in range(lower,upper + 1): 
    if num > 1: 
        for i in range(2,num): 
            if (num % i) == 0: 
                break 
        else: 
            print(num)
'''
# Program python untuk menentukan bilangan prima atau tidak

# Meminta input bilangan dari user
num = int(input("Masukkan bilangan: "))

# bilangan prima harus lebih besar dari 1
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "bukan bilangan prima")
            print(i, "kali", num//i, "=", num)
            break
    else:
        print(num,"adalah bilangan prima")

# bila bilangan kurang atau sama dengan satu
else:
    print(num, "bukan bilangan prima")