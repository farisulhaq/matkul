a = int(input("bilangan pertama : "))
b = int(input("bilangan kedua : "))
temp = 1
fpb = 0
for i in range(2,a+1):
    if a%i==0 and b%i==0:
        print(f'pembagi yang sama = {temp} = {i}')
        temp += 1
        fpb = i
print("pembagi yang sama yang terbesar adalah =", fpb)
