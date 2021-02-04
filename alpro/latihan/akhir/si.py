# def fungsiIO():
#     a = input("masukkan angka : ")
#     b = a.split()
#     b.sort()
#     for i in range(len(b)):
#         print("*"*int(b[i]))
# fungsiIO()

# dcur2idr = {}
# dcur2idr['USD'] = 0.8890600924499229
# def usd2eur(usd):
#     return float(usd * dcur2idr['USD'])
# print(usd2eur(100))

def caseShopia(string):
    abjad = 'abcdefghijklmnopqrstuvwxyz'
    a = abjad.upper()
    b = abjad.lower()
    konvert = ''
    for i in string:
        for j in range(len(abjad)):
            if i in a[j] or i in b[j]:
                konvert += i
    konvert = konvert.swapcase()
    return konvert

