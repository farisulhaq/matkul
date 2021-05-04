# 200411100171 Ahmad Farisul Haq
# Fingsi Display
def display(data):
    temp = ""
    for i in data[1]:
        temp += f'|{i}|\n'
    return temp
# Fungsi Tower Of Hanoi
def hanoi(n, awal, bantuan, tujuan):
    if n == 0:
        return
    else:
        hanoi(n - 1, awal, tujuan, bantuan)
        tujuan[1].insert(0,awal[1].pop(0))
        print(f'lempengan - {n} dari - {awal[0]} ke - {tujuan[0]}')
        print(f'A:\n{display(A)}\nB:\n{display(B)}\nC:\n{display(C)}')
        hanoi(n - 1, bantuan, awal, tujuan)
# main 
n = int(input("Banyak Element : "))
A = ["A",[x for x in range(1,n+1)]]
B = ["B",[]]
C = ["C",[]]
# print Data Awal
print(f"Perpindahan {n} Lempengan dari A ke C dengan menggunakan Bantuan B")
print(f'A:\n{display(A)}\nB:\n{display(B)}\nC:\n{display(C)}')
# pemanggilan fungsi
hanoi(n,A,B,C)
