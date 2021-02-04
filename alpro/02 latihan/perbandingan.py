nama = {
    "jaka" : 1100,
    "ida" : 1000
}
nilai = {
    "jaka" : 3.5,
    "ida" : 3.5
}
for i in nama:
    if nama[i] > 1100 and nilai[i] >= 3.0:
        print(i, "lulus persyaratan")
    else:
        print(i, "tidak lulus persyaratan")