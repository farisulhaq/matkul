# Ahmad Farisul Haq
# 200411100171
from tkinter import messagebox

# --- fungsi membuat matriks --- #
def createSparseMatrix():
    matx = {}
    row = int(input('jumlah baris = '))
    col = int(input('Jumlah kolom = '))
    elm = int(input('Jumlah elemen = '))
    while len(matx) < elm:
        stop = False
        baris = int(input('Baris ke- ? '))
        if baris < row:
            while not(stop):
                kolom = int(input('Kolom ke- ? '))
                if kolom >= col:
                    messagebox.showerror('Eror','Indeks Kolom Maksimum = {}'.format(col))
                else:
                    data = int(input(f'data ({baris},{kolom}) = '))
                    matx[baris,kolom] = data
                    stop = True
        else:
           messagebox.showerror('Eror','Indeks Baris Maksimum = {}'.format(row)) 
    return matx,row,col
# --- fungsi Penjumlahan matriks --- #
def addSparceMatrix(matx1,matx2,row,col):
    juml = {}
    for x in range(row):
        for y in range(col):
            data = matx1.get((x,y),0)+matx2.get((x,y),0)
            juml[x,y] = data
    return juml
# --- fungsi perkalian matriks --- #
def multSparseMatrix(matx1,matx2,row1,col1,row2,col2):
    mult = {}
    for x in range(row1):
        for y in range(col2):
            nilai = 0
            for z in range(col1):
                nilai += matx1.get((x,z),0) * matx2.get((z,y),0)
            mult[x,y] = nilai
    return mult
# --- fungsi display --- #
# def displayData(matx,row,col):
#     for x in range(row):
#         print('|',end='')
#         for y in range(col):
#             # --- cv ke string --- #
#             data = str(matx.get((x,y),0))
#             print(' '*(4-len(data))+data, end='')
#         print('   |')
#     print('-----------------------')
def displayData(matx,row,col):
    for x in range(row):
        print('|',end='')
        for y in range(col):
            # --- cv ke string --- #
            data = (matx.get((x,y),0))
            print('%4d'%data, end='')
        print('%4s'%'|')
    print('-----------------------')
# ---------------------------- Main ---------------------------- #
# -- Create Matrix -- #
(matrix1,row1,col1) = createSparseMatrix()
print('Matriks 1 = ',matrix1)
print('------------------------')
(matrix2,row2,col2) = createSparseMatrix()
print('Matriks 2 = ',matrix2)
print('------------------------')
# -- pernyataan -- #
print('1. penjumlahan\n2. perkalian')
inp = int(input('masukkan pilihan (1/2) : '))
if inp == 1:
    # --- Add Matrices --- #
    if row1 == row2 and col1 == col2:
        matrixSum = addSparceMatrix(matrix1,matrix2,row1,col1)
        displayData(matrix1,row1,col1)
        displayData(matrix2,row2,col2)
        displayData(matrixSum,row1,col1)
    else:
        messagebox.showerror('Eror','Ukuran Matriks Tidak Sama')
else:
    # -- Mult Matrices -- #
    if col1 == row2:
        matrixmult = multSparseMatrix(matrix1,matrix2,row1,col1,row2,col2)
        displayData(matrix1,row1,col1)
        displayData(matrix2,row2,col2)
        displayData(matrixmult,row1,col2)
    else:
        messagebox.showerror('Eror','Ukuran Matriks Tidak Sama')