# import sys
# from functools import partial
# # import module from pyqt5
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QGridLayout
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtWidgets import QVBoxLayout
# from PyQt5.QtWidgets import QMainWindow
# from PyQt5.QtWidgets import QWidget
# from PyQt5.QtWidgets import QLineEdit
# from PyQt5.QtWidgets import QApplication
 
# class CalcUI(QMainWindow):
#     def __init__(self):
#         # initialize view
#         super().__init__()
 
#         # set main window properties
#         self.setWindowTitle("Kalkulator")
#         self.setFixedSize(235, 235)
 
#         # set central widget and general layout
#         self.generalLayout = QVBoxLayout()
#         self._centralWidget = QWidget(self)
#         self.setCentralWidget(self._centralWidget)
#         self._centralWidget.setLayout(self.generalLayout)
 
#         # create display and button object
#         self._createDisplay()
#         self._createButton()
 
#     # create function display
#     def _createDisplay(self):
#         # creating display
#         self.display = QLineEdit()
 
#         #  set display properties
#         self.display.setFixedHeight(35)
#         self.display.setAlignment(Qt.AlignRight)
#         self.display.setReadOnly(True)
 
#         # add display to general layout
#         self.generalLayout.addWidget(self.display)
 
#     # create function _createButton
#     def _createButton(self):
#         self.buttons = {}
 
#         # set layout
#         buttonsLayout = QGridLayout()
 
#         # button text    | position on grid layout
#         buttons = {'7': (0, 0),
#                    '8': (0, 1),
#                    '9': (0, 2),
#                    '/': (0, 3),
#                    'C': (0, 4),
#                    '4': (1, 0),
#                    '5': (1, 1),
#                    '6': (1, 2),
#                    '*': (1, 3),
#                    '(': (1, 4),
#                    '1': (2, 0),
#                    '2': (2, 1),
#                    '3': (2, 2),
#                    '-': (2, 3),
#                    ')': (2, 4),
#                    '0': (3, 0),
#                    '00': (3, 1),
#                    '.': (3, 2),
#                    '+': (3, 3),
#                    '=': (3, 4),
#                    }
 
#         # create button and add to grid layout
#         for btnText, position in buttons.items():
#             self.buttons[btnText] = QPushButton(btnText)
#             self.buttons[btnText].setFixedSize(40,40)
#             buttonsLayout.addWidget(self.buttons[btnText], position[0],position[1])
 
#         # add button layout to general layout
#         self.generalLayout.addLayout(buttonsLayout)
 
 
#     def setDisplayText(self, text):
#         self.display.setText(text)
#         self.display.setFocus()
 
#     def displayText(self):
#         return self.display.text()
 
#     def clearDisplay(self):
#         self.setDisplayText('')
 
# # create controller
# class CalcController:
#     def __init__(self, model, views):
#         # inisialize controler
#         self._views = views
#         self._evaluate = model
 
#         # connecting to signal and slots
#         self._connectSignals()
 
#     # calculate result
#     def _calculateResult(self):
#         result = self._evaluate(expression=self._views.displayText())
#         self._views.setDisplayText(result)
 
#     def _buildExpression(self, sub_exp):
#         if self._views.displayText() == ERROR_MSG:
#             self._views.clearDisplay()
#         expression = self._views.displayText() + sub_exp
#         self._views.setDisplayText(expression)
 
#     def _connectSignals(self):
#         # connect to signal
#         for btnText, btn in self._views.buttons.items():
#             if btnText not in {'=':'C'}:
#                 btn.clicked.connect(partial(self._buildExpression, btnText))
#         self._views.buttons['='].clicked.connect(self._calculateResult)
#         self._views.display.returnPressed.connect(self._calculateResult)
#         self._views.buttons['C'].clicked.connect(self._views.clearDisplay)
 
# # Error Message
# ERROR_MSG = 'Errors'
 
# # create model
# def evaluateExpressionModel(expression):
#     # evaluate expression
#     try:
#         result = str(eval(expression, {}, {}))
#     except Exception:
#         result = ERROR_MSG
 
#     return result
 
 
# # client mode
# def main():
#     pycalc = QApplication(sys.argv)
#     views = CalcUI()
#     views.show()
#     #  create instance model of controller
#     model = evaluateExpressionModel
#     CalcController(model=model, views=views)
 
#     sys.exit(pycalc.exec_())
# if __name__ == '__main__':
#     main()

# from functools import partial
# import tkinter as tk


# class applikasiKalkulator(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title("Kalkulator tkinter")
#         self.membuatTombol()
#         self.penentu = False

#     def membuatTombol(self):
#         self.layar = tk.Entry(self, width=25)
#         self.layar.grid(row=0, column=0, columnspan=5)

#         btn_list = [
#             '1', '2', '3',
#             '4', '5', '6',
#             '7', '8', '9',
#             '0', '+', '-',
#             'C', '/', '*',
#             '='
#         ]
#         baris = 1
#         kolom = 0
#         for penampung in btn_list:
#             perintah = partial(self.hitung, penampung)
#             if penampung == '=':
#                 tk.Button(self, text='=', width=22, command=perintah).grid(row=baris, column=kolom, columnspan=5)
#             else :
#                 tk.Button(self, text=penampung, width=5, command=perintah).grid(row=baris, column=kolom)
#             kolom += 1
#             if kolom > 2:
#                 kolom = 0
#                 baris += 1

#     def hitung(self, key):
#         if key == '=':
#             self.penentu = True
#             try:
#                 result = eval(self.layar.get())
#                 self.layar.delete(0, tk.END)
#                 self.layar.insert(tk.END, str(result))
#             except:
#                 self.layar.insert(tk.END, "-> Error!")
#         elif key == 'C':
#             self.layar.delete(0, tk.END)
#         else:
#             if self.penentu :
#                 self.layar.delete(0, tk.END)
#                 self.penentu = False
#             self.layar.insert(tk.END, key)

# panggil = applikasiKalkulator()
# panggil.mainloop()

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
            gudang = []
            penampung = ''
            hasil = 1
            
            for i in range (len(masukan)):
                if masukan[i] == '0' or masukan[i] == '1' or masukan[i] == '2' or masukan[i] == '3' or masukan[i] == '4' or masukan[i] == '5' or masukan[i] == '6' or masukan[i] == '7' or masukan[i] == '8' or masukan[i] == '9'  :
                    penampung += masukan[i]
                else :
                    a = int(penampung)
                    gudang.append(a)
                    gudang.append(masukan[i])
                    penampung = ''
                    
            a = int(penampung)
            gudang.append(a)
                    
            
            i = 0   
            while i < len(gudang) :
                if gudang[i] == '*' :
                    gudang.pop(i)
                    hasil = gudang.pop(i-1)*gudang.pop(i-1)
                    gudang.insert(i-1, hasil)
                    i = 0
                i+=1
            
            i = 0   
            while i < len(gudang) :
                if gudang[i] == '/' :
                    gudang.pop(i)
                    hasil = gudang.pop(i-1)/gudang.pop(i-1)
                    gudang.insert(i-1, hasil)
                    i = 0
                i+=1
            
            i = 0   
            while i < len(gudang) :
                if gudang[i] == '-' :
                    gudang.pop(i)
                    hasil = gudang.pop(i-1)-gudang.pop(i-1)
                    gudang.insert(i-1, hasil)
                    i = 0
                i+=1
            
            i = 0   
            while i < len(gudang) :
                if gudang[i] == '+' :
                    gudang.pop(i)
                    hasil = gudang.pop(i-1)+gudang.pop(i-1)
                    gudang.insert(i-1, hasil)
                    i = 0
                i+=1
            
            hasil = str(gudang.pop())
            hasil = "hasilnya adalah : " + hasil
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