kalimat = input("masukkan kalimat = ")
v = 0
k = 0
vokal = " "
konsonan = " "
spasi = 0
a = 'aiueo'
for huruf in kalimat:
    if huruf.lower() in a:
        vokal += huruf + " "
        v += 1
    elif huruf.lower() not in a:
        konsonan += huruf + " "
        k += 1
    else:
        spasi += 1

print("jumlah huruf Vokal = ", v, ", yaitu :", vokal)
print("jumlah huruf konsonan = ", k, ", yaitu :", konsonan)
print("jumlah spasi = ",spasi)