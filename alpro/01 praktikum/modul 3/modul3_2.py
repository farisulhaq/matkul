num = int(input("masukkan angka : "))
r_ribuan = ["","M", "MM", "MMM"]
r_ratusan = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
r_puluhan = ["","X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
r_satuan = ["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
rb = r_ribuan[int(num/1000)]
rs = r_ratusan[int((num/100)%10)]
p = r_puluhan[int((num%100)/10)]
s = r_satuan[int(num%10)]
print("bentuk dalam romawi :",rb+rs+p+s)