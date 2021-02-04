kalimat = input("masukkan kalimat = ")
huruf = input("masukkan huruf yang dicari = ")
temp = 0
offset = 0
for i in kalimat:
    if i == huruf:
        temp += 1
        print("huruf", huruf.lower(), "huruf", huruf.upper(), "ke-", temp, ": offset-", offset)
    offset += 1