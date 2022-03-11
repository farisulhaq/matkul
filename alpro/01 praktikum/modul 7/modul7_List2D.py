# fungsi membuat matriks 2D
def createMat2D(row,col):
    matriks = []
    for x in range(row):
        temp = []
        for y in range(col):
            inp = int(input(f'matrik[{x},{y}] = '))
            temp.append(inp)
        matriks.append(temp)
    return matriks
# fungsi menampilkan matriks 2D
def dispMat2D(mat,name):
    print(name)
    if mat == False:
        print('ukuran matriks salah')
    else:
        for x in range(len(mat)):
            print("|",end="")
            for y in range(len(mat[0])):
                isi = str(mat[x][y])
                print(" "*(4-len(isi))+ isi, end="")
            print("   |")
# fungsi Penjumlahan 2 Matriks 2D
def addMat(mat1,mat2):
    matriks = []
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return False
    else:
        for x in range(len(mat1)):
            temp = []
            for y in range(len(mat1[0])):
                temp.append(mat1[x][y]+mat2[x][y])
            matriks.append(temp)
        return matriks
# fungsi Perkalian 2 Matriks 2D
def multMat(mat1,mat2):
    matriks = []
    if len(mat1[0]) != len(mat2):
        return False
    else:
        for x in range(len(mat1)):
            temp = []
            for y in range(len(mat2[0])):
                isi = 0
                for z in range(len(mat1[0])):
                    isi += mat1[x][z]*mat2[z][y]
                temp.append(isi)
            matriks.append(temp)
        return matriks
# main program #
# create matriks
print('Create Mat 1')
Matriks1 = createMat2D(4,4)
print('Create Mat 2')
Matriks2 = createMat2D(4,4)
print('Create Mat 3')
Matriks3 = createMat2D(3,2)
# menampilkan matriks
dispMat2D(Matriks1,'Matrik 1 =')
dispMat2D(Matriks2,'Matrik 2 =')
# penjumlahan 2 matriks 2D
hasilJumlah = addMat(Matriks1,Matriks2)
# menampilkan penjumlahan 2 matriks
dispMat2D(hasilJumlah,'Matriks 1 + Matriks 2 =')
# penjumlahan 2 matriks 2D
hasilJumlah = addMat(Matriks1,Matriks3)
dispMat2D(hasilJumlah,'Matriks 1 + Matriks 3 =')
# perkalian 2 matriks 2D
hasil = multMat(Matriks1,Matriks3)
dispMat2D(Matriks1,'Matrik 1 =')
dispMat2D(Matriks3,'Matrik 3 =')
# menampilkan perkalian 2 matriks
dispMat2D(hasil,'Matriks 1 * Matriks 3 =')
# perkalian 2 matriks 2D
hasil = multMat(Matriks1,Matriks2)
dispMat2D(hasil,'Matriks 1 * Matriks 2 =')