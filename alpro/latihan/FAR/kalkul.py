def jumlah(a,b):
    return int(a) + int(b)
def kurangi(a,b):
    return a - b
def kali(a,b):
    return a * b
def bagi(a,b):
    return a / b

# a = input("kuntul = ")
# a = a.replace('+','')
# a = a.split()
# x = a[0]
# y = 1
# start = True
# while start:
#     x = jumlah(int(x),int(a[y]))
#     y += 1
#     if y == len(a):
#         start = False
#     print(x)

# 2
# a = "1 + 2 - 3 - 4"
# b = a
# code = "+-x/"
# for i in code :
#     b = b.replace(i,"")
# c = a
# code = "0123456789"
# for i in code :
#     c = c.replace(i,"")

# 3
# b = b.split()
# c = c.split()
# for i in c:
#     x = b[0]
#     y = 1
#     if i == "+":
#         start = True
#         while start:
#             x = jumlah(int(x),int(b[y]))
#             y += 1
#             if y == len(b):
#                 start = False
#         print(x)

# 4
# a = input(" kun = ")
# b = a.split()
# x = b[0]
# y = 2
# for i in range(1,len(b),2):
#     if b[i] == "+":
#         x = jumlah(int(x),int(b[y]))
#     elif b[i] == "-":
#         x = kurangi(int(x),int(b[y]))
#     # elif b[i] == "*":
#     #     x = kali(int(x),int(b[y]))
#     elif b[i] == "/":
#         x = bagi(int(x),int(b[y]))
#     else:
#         print(x)
#     y += 1

# 5
# import operator

# ops = {
#     '+' : operator.add,
#     '-' : operator.sub,
#     '*' : operator.mul,
#     '/' : operator.truediv
# }

# def basic_op(oper, v1, v2):
#     return ops[oper](v1,v2)

# 6
# b = masukan.split()
#         i = 0
#         while i < len(b) :
#             if b[i] == '*' :
#                 b.pop(i)
#                 kuntul = float(b.pop(i-1))*float(b.pop(i-1))
#                 b.insert(i-1, kuntul)
#                 i = 0
#             i+=1
#         i = 0   
#         while i < len(b) :
#             if b[i] == '/' :
#                 b.pop(i)
#                 kuntul = float(b.pop(i-1))/float(b.pop(i-1))
#                 b.insert(i-1, kuntul)
#                 i = 0
#             i+=1
#         i = 0
#         while i < len(b) :
#             if b[i] == '-' :
#                 b.pop(i)
#                 kuntul = float(b.pop(i-1))-float(b.pop(i-1))
#                 b.insert(i-1, kuntul)
#                 i = 0
#             i+=1
#         i = 0
#         while i < len(b) :
#             if b[i] == '+' :
#                 b.pop(i)
#                 kuntul = float(b.pop(i-1))+float(b.pop(i-1))
#                 b.insert(i-1, kuntul)
#                 i = 0
#             i+=1

import tkinter as tk # mengimpor modul tkinter dan menamakannya tk
from tkinter import Text
from tkinter.messagebox import showinfo

class Application(tk.Frame): # membuat class Application sebagai warisan dari class Frame milik tkinter
    def __init__(self, master=None): # ini adalah constructor dari class Frame dan akan dijalankan pertama kali
        tk.Frame.__init__(self, master) # menjalankan contructor
        self.grid() # menampilkan window utama ke screen
        self.createWidgets()
        
        
    def createWidgets(self):
        # first field
        self.field1 = tk.Entry(self,width=20) # membuat field isian bilangan pertama
        self.field1.insert(0, "") # isian dikosongkan
        self.field1.grid(row=0,column=0) # posisi widget dalam grid
        self.field1.insert(0, "Masukkan angka")
        
        
        # ADD button
        self.ADD = tk.Button(self) # membuat ADD button
        self.ADD["text"] = "jalankan" # tulisan pada button
        self.ADD["command"] = self.add_numbers # method yang akan dijalankan jika button di-klik
        self.ADD.grid(row=0,column=1) # posisi widget dalam grid             

    def add_numbers(self): # method untuk menjumlahkan dua angka
        try :
            masukan = self.field1.get() # mengambil angka dari isian pertama
            b = masukan.split()
            i = 0
            while i < len(b) :
                if b[i] == '*' :
                    b.pop(i)
                    kuntul = float(b.pop(i-1))*float(b.pop(i-1))
                    b.insert(i-1, kuntul)
                    i = 0
                i+=1
            i = 0   
            while i < len(b) :
                if b[i] == '/' :
                    b.pop(i)
                    kuntul = float(b.pop(i-1))/float(b.pop(i-1))
                    b.insert(i-1, kuntul)
                    i = 0
                i+=1
            i = 0
            while i < len(b) :
                if b[i] == '-' :
                    b.pop(i)
                    kuntul = float(b.pop(i-1))-float(b.pop(i-1))
                    b.insert(i-1, kuntul)
                    i = 0
                i+=1
            i = 0
            while i < len(b) :
                if b[i] == '+' :
                    b.pop(i)
                    kuntul = float(b.pop(i-1))+float(b.pop(i-1))
                    b.insert(i-1, kuntul)
                    i = 0
                i+=1
            
            kuntul = str(b.pop())
            hasil = "hasilnya adalah : " + kuntul
            showinfo("Hasil", hasil)
        except :
            showinfo("Pesan","Maaf ada yang salah.")

root = tk.Tk()

# modify root window

root.title("Kalkulator string") # title window aplikasi
root.geometry("300x200") # panjang dan tinggi window aplikasi
root.configure(bg='grey')

app = Application(master=root)
app.mainloop()