rmw = input("masukkan romawi : ")
a, b, hasil = 0, 0, 0
romawi = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L" : 50,
    "X" : 10,
    "V" : 5,
    "I" : 1
}
for i in rmw.upper():
    if i in romawi:
        a = romawi[i]
        if a > b:
            hasil = hasil + a - 2*b
        else:
            hasil += a
        b = a
print(rmw, "=", hasil)


