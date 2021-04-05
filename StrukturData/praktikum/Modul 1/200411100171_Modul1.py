from sparseMatrix import *
# ---------------------------- Main ---------------------------- #
# -- Create Matrix -- #
print('Matriks 1 = ')
(matrix1,row1,col1) = createSparseMatrix()
print('------------------------')
print('Matriks 2 = ')
(matrix2,row2,col2) = createSparseMatrix()
print('------------------------')
# Menampilkan Matriks
print('matrik 1 = ')
displayData(matrix1,row1,col1)
print('matrik 2 = ')
displayData(matrix2,row2,col2)
# perkalian Matriks
if col1 == row2:
    print('Hasil Perkalian Matriks')
    matrixmult = multSparseMatrix(matrix1,matrix2,row1,col1,row2,col2)
    print('matrik 1 = ')
    displayData(matrix1,row1,col1)
    print('matrik 2 = ')
    displayData(matrix2,row2,col2)
    print('Hasil = ')
    displayData(matrixmult,row1,col2)
else:
    print('Eror','Ukuran Matriks Tidak Sama')