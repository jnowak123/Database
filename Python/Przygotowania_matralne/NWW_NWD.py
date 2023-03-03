a, b = 44, 32

def NWD(a, b):
    while b != 0:
        c = a%b
        a, b = b, c
    return a

def NWW(a, b):
    return (round((a*b)/NWD(a, b)))

print(NWD(a, b))
print(NWW(a, b))