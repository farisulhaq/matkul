#fungsi buat matriks2D
def createMat2D(row,col):
    #list kosong
    mat=[]
    #looping baris
    for i in range (row):
        temp=[]
        #looping kolom
        for j in range (col):
            bil=int(input("Matriks["+str(i)+","+str(j)+"]="))
            temp.append(bil)
        mat.append(temp)
    return mat
#fungsi menampilkan matriks2D
def dispMat2D(mat,nama):
    #jika ukuran tidak sama
    if (mat == False):
        print("ukuran matrik salah")
    else:
        print(nama)
    #mencetak matriks2D
    for x in range(len(mat)):
            print("|", end="")
            for y in range(len(mat[x])):
                #konversi ke string
                data = str(mat[x][y])
                #penambahan spasi
                print(" "*(4-len(data)) + data, end="")
            print("  |")
#fungsi penjumlahan
def addMat(mat1,mat2):
    jml = []
    #cek ukuran
    if (len(mat1) != len(mat2) and len(mat1[0]) != len(mat2[0])):
        return False
    #penjumlahan
    for x in range(len(mat1)):
        tmp = []
        for y in range(len(mat1[x])):
            tmp.append(mat1[x][y] + mat2[x][y])
        jml.append(tmp)
    return jml
#fungsi perkalian
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
#main program
#membuat matriks
print("Create Mat 1")
matriks1=createMat2D(2,3)
print("Create Mat 2")
matriks2=createMat2D(2,3)
print("Create Mat 3")
matriks3=createMat2D(3,2)
#menampilkan matriks yang sudah dibuat
dispMat2D(matriks1,"Matrik1=")
dispMat2D(matriks2,"Matrik2=")
dispMat2D(matriks3,"Matrik3=")
#memanggil fungsi penjumlahan
hjumlah=addMat(matriks1,matriks2)
#menampilkan hasil penjumlahan
dispMat2D(hjumlah,"Matriks1+Matriks2=")
#memanggil fungsi perkalian
hkali=multMat(matriks1,matriks3)
#menampilkan hasil perkalian
dispMat2D(hkali,"Matriks1*Matriks3=")