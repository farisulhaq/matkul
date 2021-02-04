from tkinter import messagebox

# --- fungsi membuat matriks --- #
def createSparseMatrix():
    matx = {}
    row = int(input('jumlah baris = '))
    col = int(input('Jumlah kolom = '))
    elm = int(input('Jumlah elemen = '))
    while len(matx) < elm:
        stop = False
        baris = int(input('Baris ke- ?'))
        if baris < row:
            while not(stop):
                kolom = int(input('Kolom ke- ?'))
                if kolom >= col:
                    messagebox.showerror('SAYANG FEBI','Indeks Kolom Maksimum = {}'.format(col))
                else:
                    data = int(input(f'data ({baris},{kolom}) = '))
                    matx[baris,kolom] = data
                    stop = True
        else:
           messagebox.showerror('SAYANG FEBI','Indeks Baris Maksimum = {}'.format(row)) 
    return matx,row,col
# --- fungsi Penjumlahan matriks --- #
def addSparceMatrix(matx1,matx2,row,col):
    juml = {}
    for x in range(row):
        for y in range(col):
            data = matx1.get((x,y),0)+matx2.get((x,y),0)
            juml[x,y] = data
    return juml
# --- fungsi display --- #
def displayData(matx,row,col):
    for x in range(row):
        print('|',end='')
        for y in range(col):
            # --- cv ke string --- #
            data = str(matx.get((x,y),0))
            print(' '*(4-len(data))+data, end='')
        print('   |')
    print('-----------------------')
# --- Main --- #
(matrik1,row1,col1) = createSparseMatrix()
print('Matriks 1 = ',matrik1)
print('-----------------------')
(matrik2,row2,col2) = createSparseMatrix()
print('Matriks 1 = ',matrik2)
print('-----------------------')
# --- Add Matrices --- #
if row1 == row2 and col1 == col2:
    matrixSum = addSparceMatrix(matrik1,matrik2,row1,col1)
    displayData(matrik1,row1,col1)
    displayData(matrik2,row2,col2)
    displayData(matrixSum,row1,col1)
else:
    messagebox.showerror('Eror','Ukuran Matriks Tidak Sama')