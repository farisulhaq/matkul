from tkinter import messagebox
def createSparceMatrix():
    mat = {}
    row = int(input('Jumlah baris = '))
    col = int(input('Jumlah kolom = '))
    elm = int(input('Jumlah elemen = '))
    while len(mat) < elm:
        stop = False
        baris = int(input('Baris ke- ?'))
        if baris < row:
            while not(stop):
                kolom = int(input('Kolom ke- ?'))      
                if kolom >= col:
                    messagebox.showerror('Eror','Indeks kolom maksium = 2')
                else:
                    data = int(input('data ('+str(baris)+','+str(kolom)+') = '))
                    mat[baris,kolom]=data
                    stop = True
        else:
            messagebox.showerror('Eror','Indek baris maksimum = 3')
    return mat,row,col
a,b,c = createSparceMatrix()
print(a)
d,e,f = createSparceMatrix()
print(d)