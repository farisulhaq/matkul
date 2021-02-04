mau = input('mau tau program saya?')
while mau=='mau':
    a=input('lanjut? y/t')
    if a=='y':
        print('pilih opsi :')
        print('ketik 1 untuk luas lingkaran')
        print('ketik 2 untuk luas persegi')
        print('ketik 3 untuk luas segitiga')
        opsi=int(input('masukkan pilihan anda'))
        if opsi == 1:
            print('masukkan jari-jari')
            r = int(input())
            phi = float(22) / 7
            lL = phi * r * r
            print('luas=', (lL), 'cm2')
        elif opsi == 2:
            print('masukkan panjang')
            p = int(input())
            print('masukkan lebar')
            l = int(input())
            lPP = p * l
            print('luas=', lPP, 'cm2')
        elif opsi == 3:
            print('masukkan alas')
            a = int(input())
            print('masukkan tinggi')
            t = int(input())
            lS = float(1) / 2 * a * t
            print("luas =",lS,"cm2")
        else:
            print('pilih yang sesuai!')
    elif a == 't':
        break
    else:
        print('pilih yang sesuai!')
print('terima kasih')