def display(mat):
    for x in range(len(mat)):
        print("|",end="")
        for y in range(len(mat[0])):
            isi = str(mat[x][y])
            print(" "*(4-len(isi))+ isi, end="   ")
        print("|")
def maxmat(mat,opsi):
    if opsi=='baris':
        baris=[]
        for i in range(len(mat)):
            maks=[]
            mak=0
            for u in range(len(mat[0])):
                if mak<mat[i][u]:
                    mak=mat[i][u]
            maks.append(mak)
            baris.append(maks)
        return baris

a = [[1,2,3],[4,5,6]]
b =maxmat(a,'baris')
display(b)