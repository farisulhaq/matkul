# a = [1,4,2,3,5]
# for i in range(len(a)):
#     print("perulangan",i)
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#         print(a)


def lingkaran(r,x=0):
    return (22/7)**r
def persegi(s,x=0):
    return s*s
def segitiga(a,t):
    return 1/2*a*t
def main(a,b=0,fuct=0):
    return(fuct(a,b))
print(main(7,persegi))
