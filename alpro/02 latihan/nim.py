a = 6
for i in range(a+1):
    print(" "*3,end="")
    print("x")
for i in range(a+1):
    print("x",end="")
print()
b = a
for i in range(b):
    for j in reversed(range(b)):
        print(" ", end="")
    for i in range(1):
        print("x",end="")
    b -= 1
    print()
for i in range(a+1):
    print(" "*3,end="")
    print("x")
a = 6
for i in range(a+1):
    print("x",end="")
print()
for i in range(a-1):
    print("x",end="")
    print(" "*(a-1),end="")
    print("x")
for i in range(a+1):
    print("x",end="")
print("\n")
for i in range(a+1):
    print("x",end="")
print()
for i in range(a-4):
    print("x",end="")
    print(" "*(a-1),end="")
    print("x")
for i in range(a+1):
    print("x",end="")
print()
for i in range(a-4):
    print("x",end="")
    print(" "*(a-1),end="")
    print("x")
for i in range(a+1):
    print("x",end="")
print("\n")
for i in range(a+1):
    print("x",end="")
print()
for i in range(a):
    for j in range(a):
        print(" ", end="")
    for i in range(1):
        print("x",end="")
    a -= 1
    print()
