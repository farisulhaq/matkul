uang = int(input('Masukkan uang anda : '))
pecahan = [100000,50000,20000,10000,5000,2000,1000]
strPecahan = ['seratus ribu','lima puluh ribu','dua puluh ribu','sepuluh ribu','lima ribu','dua ribu','seribu']

sisa = uang
for i in range(len(pecahan)) :
    bagi = sisa//pecahan[i]
    print (bagi, 'lembar', strPecahan[i])
    sisa = sisa % pecahan[i]

# uang = int(input("masukkan uang : "))
# dic = {
#     100000 : 'seratus ribu',
#     50000 : 'lima puluh ribu',
#     20000 : 'dua puluh ribu',
#     10000 : 'sepuluh ribu',
#     5000 : 'lima ribu',
#     2000 : 'dua ribu',
#     1000 : 'seribu'
# }
# sisa = uang
# for i in dic:
#     hsl = sisa // i
#     sisa %= i
#     print(hsl,'lembar',dic[i])
    
# a = ['rama','saya']
# b = [2,1]
# c = a.index('saya')
# b[c] += 1
# print(c)
# print(b)
