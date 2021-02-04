def createSparseMatrix(row,col):
    mat = {}
    mat['baris'] = row
    mat['kolom'] = col
    ele = int(input('Jumlah data yang tidak nol ? '))
    i = 1
    while i <= ele:
        print('Data ke-',i)
        baris = int(input('Indeks Baris ke - '))
        kolom = int(input('Indeks Kolom ke - '))
        if baris < row and kolom < col:
            data = int(input('sparseMat['+str(baris)+','+str(kolom)+'] = '))
            mat[baris,kolom] = data
            i += 1
        else:
            print('indeks baris atau kolom melebihi jumlah baris atau kolom')
    return mat
def dispSparseMatrix2D(mat):
    row = mat['baris']
    col = mat['kolom']
    cetak = ''
    for i in range(row):
        isi = ''
        for j in range(col):
            data = str(mat.get((i,j),0))
            key = ' '*(4-len(data))+data
            isi += key
        cetak += '|'+isi+'   |\n'
    return cetak
def addSparseMatrix(mat1,mat2):
    row1 = mat1['baris']
    col1 = mat1['kolom']
    row2 = mat2['baris']
    col2 = mat2['kolom']
    addSM = {}
    addSM['baris'] = row1
    addSM['kolom'] = col1
    if row1 == row2 and col1 == col2:
        for i in range(row1):
            for j in range(col1):
                data = mat1.get((i,j),0) + mat2.get((i,j),0)
                addSM[i,j] = data
        return addSM
    else:
        return False
def multSparseMat(mat1,mat2):
    row1 = mat1['baris']
    col1 = mat1['kolom']
    row2 = mat2['baris']
    col2 = mat2['kolom']
    multSM = {}
    multSM['baris'] = row1
    multSM['kolom'] = col2
    if col1 == row2:
        for x in range(row1):
            for y in range(col2):
                isi = 0
                for z in range(col1):
                    isi += mat1.get((x,z),0) * mat2.get((z,y),0)
                multSM[x,y] = isi
        return multSM
    else:
        return False

mat1 = createSparseMatrix(5,4)
mat2 = createSparseMatrix(5,4)
print('Sparse Matriks 1 :')
print(dispSparseMatrix2D(mat1))
print('Sparse Matriks 2 :')
print(dispSparseMatrix2D(mat2))
hasilJumlah = addSparseMatrix(mat1,mat2)
if hasilJumlah == False:
    print('Ukuran Tidak Sama')
else:
    print('Hasil Penjumlahan :')
    print(dispSparseMatrix2D(hasilJumlah))