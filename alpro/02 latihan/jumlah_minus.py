l1 = []
l2 = []
stop = False
while not(stop):
    l1.append(float(input("masukkan data ke list 1 : ")))
    a = input("input y to continue = ")
    if a == "y":
        stop = False
    else:
        print("list 1 = ",l1)
        while not(stop):
            l2.append(float(input("masukkan data ke list 2 : ")))
            b = input("input y to continue = ")
            if b == "y":
                stop = False
            else:
                print("list 2 =",l2)


