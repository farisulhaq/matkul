a = 5
b = ''
while a > 0:
    b += str(a%2)
    a //= 2
print(b[::-1])