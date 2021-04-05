# --- fungsi membuat matriks --- #
def createSparseMatrix():
    matx = {}
    row = int(input('Jumlah baris = '))
    col = int(input('Jumlah kolom = '))
    elm = int(input('Jumlah data = '))
    while len(matx) < elm:
        stop = False
        baris = int(input('Baris ke- ? '))
        if baris < row:
            while not(stop):
                kolom = int(input('Kolom ke- ? '))
                if kolom >= col:
                    print('Eror','Indeks Kolom Maksimum = {}'.format(col))
                else:
                    data = int(input(f'matrik [{baris},{kolom}] = '))
                    matx[baris,kolom] = data
                    stop = True
        else:
           print('Eror','Indeks Baris Maksimum = {}'.format(row)) 
    return matx,row,col
# --- fungsi display --- #
def displayData(matx,row,col):
    for x in range(row):
        print('|',end='')
        for y in range(col):
            # --- cv ke string --- #
            data = (matx.get((x,y),0))
            print('%4s'%data, end='')
        print('%4s'%'|')
    print('-----------------------')
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