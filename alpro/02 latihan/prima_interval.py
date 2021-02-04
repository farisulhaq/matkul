# a = int(input("masukkan batas bawah : "))
# b = int(input("masukkan batas atas : "))
# for x in range(a,b+1):
#     if x > 1:
#         for i in range(2,x):
#             if x%i==0:
#                 break
#         else:
#             print(x)
mat1 = [[1,2],[3,4,5]]
print(len(mat1[1]))
for x in range(len(mat1)):
    for y in range(len(mat1)):
        for z in range(len(mat1[0])):
            print(x,y,z)