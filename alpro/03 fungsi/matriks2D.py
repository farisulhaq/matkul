def matriks(a,b):
    data = []
    for x in range(a):
        tem = []
        for y in range(b):
            tem.append(int(input(f'matriks {x},{y} = ')))
        data.append(tem)
    return data
def multMat(mat1,mat2):
    jml = []
    #cek ukuran
    if (len(mat1) != len(mat2[0]) and len(mat1[0]) != len(mat2)):
        return False
    #perkalian
    for x in range(len(mat1)):
        tmp = []
        for y in range(len(mat1)):
            bil = 0
            for z in range(len(mat1[0])):
                bil += (mat1[x][z] * mat2[z][y])
            tmp.append(bil)
        jml.append(tmp)
    return jml
a = matriks(2,2)
print(a)
b = matriks(2,2)
print(b)
print(multMat(a,b))
