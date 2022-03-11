# def bubble(data):
#     x = len(data)
#     i = 0
#     while i < len(data)//2:
#         print("iterasi",i+1)
#         temp = 0
#         print(x-1)
#         for j in range(i,x-1):
#             if data[j] > data[j+1]:
#                 data[j],data[j+1]=data[j+1],data[j]
#                 temp += 1
#             print(data)
#         if temp == 0:
#             x = 0
#         else:
#             print("iterasi kanan ke kiri")
#             for y in reversed(range(i+1,x-1)):
#                 if data[y] < data[y-1]:
#                     data[y],data[y-1]=data[y-1],data[y]
#                 print(data)
#         x -= 1
#         i += 1
# a = [5,4,3,2,1]
# bubble(a)
def urut(nilai):
    for i in range(len(nilai)):
        for j in range(len(nilai)-1):
            if nilai[j] > nilai[j+1]:
                nilai[j],nilai[j+1]=nilai[j+1],nilai[j]
    return nilai 

a = [1,6,4,7,5,8,9,1,2,3,4]
genap = []
ganjil = []
for i  in a:
    if i % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)
print(urut(genap),urut(ganjil))
