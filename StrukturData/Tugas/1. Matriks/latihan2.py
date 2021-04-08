# ahmad farisul haq 200411100171 #
#  latihan 2
# create matriks
def creatematriks(row,col):
    matrix = [] 
    for x in range(row):
        isi = []
        for y in range(col):
            isi.append(int(input(f'matrix ({x},{y}) = ')))
        matrix.append(isi)
    return matrix
# perkalian matriks
def multmatx(matx1,matx2):
    matrik = []
    if len(matx1[0]) != len(matx2):
        return False
    else:
        for x in range(len(matx1)):
            data = []
            for y in range(len(matx2[0])):
                isi = 0
                for z in range(len(matx1[0])):
                    isi += matx1[x][z] * matx2[z][y]
                data.append(isi)
            matrik.append(data)
    return matrik    
# display matriks
def display(data,nama):
    print(nama)
    if data == False:
        print('ukuran matriks salah')
    else:
        for x in range(len(data)):
            print('|', end='')
            for y in range(len(data[x])):
                print('%4d'%data[x][y], end='')
            print('%4s'%('|'))