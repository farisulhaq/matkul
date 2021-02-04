# # insert sort
# x = [
#     [200411100171,"ahmad","sumenep","ALPRO A"],
#     [200411100170,"farhan","pamekasan","ALPRO B"],
#     [200411100169,"ahmad","sampang","ALPRO C"]
# ]
x=[['faris',87],['fina',75],['nurin',77]]
print(x,'\n')
for i in range(len(x)):
    for j in range(i,len(x)):
        if x[i][1] > x[j][1]:
            x[j],x[i] = x[i],x[j]
        print(x)
# search list
for i in range(len(x)):
    if x[i][1] == 'ahmad':
        print()
print('\n1. cari berdasarkan Nama\n2. cari berdasarkan Nim')