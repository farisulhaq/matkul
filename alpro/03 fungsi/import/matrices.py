def createMat(a,b,c):
    print(a)
    mat = []
    for i in range(b):
        isi = []
        for j in range(c):
            a = int(input("matriks("+str(i)+","+str(j)+")="))
            isi.append(a)
        mat.append(isi)
    return mat
    
def cetakMat(mat,nama):
    for i in range(len(mat)):
        print("|", end="")
        for j in range(len(mat[0])):
            isi = str(mat[i][j])
            print(" "*(4-len(isi))+ isi, end="")
        print("   |")