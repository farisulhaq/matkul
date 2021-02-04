# def dispSparseMatrix2D(mat):
#     row = mat['baris']
#     col = mat['kolom']
#     cetak = ''
#     for i in range(row):
#         isi = ''
#         for j in range(col):
#             data = str(mat.get((i,j),0))
#             key = ' '*(4-len(data))+data
#             isi += key
#         cetak += '|'+isi+'   |\n'
#     return cetak
# def multSparseMat(mat1,mat2):
#     row1 = mat1['baris']
#     col1 = mat1['kolom']
#     row2 = mat2['baris']
#     col2 = mat2['kolom']
#     multSM = {}
#     multSM['baris'] = row1
#     multSM['kolom'] = col2
#     if col1 == row2:
#         for x in range(row1):
#             for y in range(col2):
#                 isi = 0
#                 for z in range(col1):
#                     isi += mat1.get((x,z),0) * mat2.get((z,y),0)
#                 multSM[x,y] = isi
#         return multSM
# ma1 = {'baris':5,'kolom':4,(3,2):4,(4,0):7}
# ma2 = {'baris':4,'kolom':2,(2,1):6}
# kali = multSparseMat(ma1,ma2)
# print(dispSparseMatrix2D(kali))

def displayData(matx,row,col):
    for x in range(row):
        print('|',end='')
        for y in range(col):
            # --- cv ke string --- #
            data = (matx.get((x,y),0))
            print('%4d'%data, end='')
        print('%4s'%'|')
    print('-----------------------')

a = {
    (1,2) : 9,
    (2,2) :12
}
displayData(a,3,3)

