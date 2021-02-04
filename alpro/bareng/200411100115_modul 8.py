from tkinter import messagebox
#Create Matrix
def createSparseMatrix () :
    mat = { }
    row = int(input('Jumlah Baris = '))
    col = int(input('Jumlah Kolom = '))
    ele = int(input('Jumlah elemen = '))
    while len(mat) < ele:
        stop = False
        bar = int(input('Baris ke- ? '))
        if bar < row:
            while not(stop) :
                kol = int(input('Kolom ke- ? '))
                if kol < col:
                    data = int(input('data ('+str(bar)+','+str(kol)+') = '))
                    mat [bar,kol] = data
                    stop = True
                else :
                    messagebox.showerror('Error','Index kolom maksimum = '+str(col))
        else :
            messagebox.showerror('Error','Index baris maksimum = '+str(row))
    return mat,row,col
#Penjumlahan
def addSparseMatrix (matrix1,matrix2,row1,col1) :
    matrik = {}
    for a in range (row1) :
        for b in range (col1) :
            data = matrix1.get((a,b),0) + matrix2.get((a,b),0)
            matrik[a,b] = data
    return matrik
#Menampilkan
def displayData (mat,row,col) :
    for a in range (row) :
        print ('|',end='')
        for b in range (col) :
            value = str(mat.get((a,b),0))
            print(' '*(5-len(value)) + value,end='')
        print('     |')
    print('-'*30)
    
#--------------------------------------------------Main------------------------------------------------------#
# Create Matrix
(matrix1,row1,col1) = createSparseMatrix ()
print ('Matriks 1 = ',matrix1)
print('-'*30)
(matrix2,row2,col2) = createSparseMatrix ()
print ('Matriks 2 = ',matrix2)
print('-'*30)

#Add matrix
if row1 == row2 and col1 == col2 :
    matrixSum = addSparseMatrix (matrix1,matrix2,row1,col1)
    displayData(matrix1,row1,col1)
    displayData(matrix2,row2,col2)
    displayData(matrixSum,row1,col1)
else :
    messagebox.showerror('Error','Ukuran Matriks Tidak Sama')

#mult matrix
if row1 == col2:
    matrixSum = addSparseMatrix (matrix1,matrix2,row1,col1)
    displayData(matrix1,row1,col1)
    displayData(matrix2,row2,col2)
    displayData(matrixSum,row1,col1)
else :
    messagebox.showerror('Error','Ukuran Matriks Tidak Sama')