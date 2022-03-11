# # fungsi deret aritmatika
# def deret(a,b,n):
# 	if n == 1:
# 		hasil = a
# 	else:
# 		hasil = b + deret(a,b,n-1)
# 	return hasil
# # input user
# a = int(input("masukkan suku awal = "))
# b = int(input("beda beda = "))
# n = int(input("masukkan banyaknya suku = "))
# hasil = deret(a,b,n)
# print("suku ke-", n, "=", hasil)


# class pixel:
# 	def __init__(self,nama,x,y):
# 		self.nama = nama
# 		self.x = (x)
# 		self.y = (y)
# 	def moveLeft(self,data):
# 		self.x -= data
# 	def moveRight(self,data):
# 		self.x += data
# 	def moveForward(self,data):
# 		self.y += data
# 	def moveBackward(self,data):
# 		self.y -= data
# 	def distance(self,obj):
# 		return ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
# 	def display(self):
# 		print (f'{self.nama} : ({self.x},{self.y})')

# pix1 = pixel("point 1",5,7)
# pix2 = pixel("point 2",6,5)
# pix1.display()
# pix2.display()
# pix1.moveBackward(5)
# pix1.display()

def createHashTable(num):
	return [["None"]] * num
def remainder(data,num):
	return data % num
def nilai(strData):
    temp = 0
    for i in strData:
        temp += ord(i)
    return temp
def putData(data,table):
    for i in data:
        slot = remainder(nilai(i),len(table))
        if table[slot] == ['None']:
            table[slot] = [i]
        else:
            table[slot].append(i)
    return table
def searchHash(data,table):
    slot = remainder(nilai(data),len(table))
    cek = 0
    for ind,num in enumerate(table[slot]):
        if num == data:
            cek += 1
            return (f'(data {data} berada di slot ke- {slot} dan indeks ke- {ind})')
    if cek == 0:
        return (f'data {data} tidak ada')

data = ['diah','dina','andi','hadi','tiara']
hashTabel = createHashTable(11)
hashTabel = putData(data,hashTabel)
print(hashTabel)
print(searchHash('indah',hashTabel))
print(searchHash('dina',hashTabel))
print(searchHash('andi',hashTabel))
print(searchHash('hadi',hashTabel))
print(searchHash('diah',hashTabel))
