def robot(string):
    x = [0,0]
    for i in string.upper():
        if i == 'R':
            x[0] += 1
        elif i == 'L':
            x[0] -= 1
        elif i == 'U':
            x[1] += 1
        elif i == 'D':
            x[1] -= 1
    y = list(map(str,x))
    return " ".join(y)
a = robot("RU")
print(a)