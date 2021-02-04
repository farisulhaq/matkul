def aku(c,b):
    a = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    for i in range(len(a)):
        if c.upper() == a[i]:
            return (a[(i + b) % 12])
a = aku('E',18)   
print(a)
def ak():
    a = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    return str(a)
print(ak)
    
            
