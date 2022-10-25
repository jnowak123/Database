from cmath import sqrt


num = []
with open("matura probna 1/dane/liczby.txt") as f:
    for line in f:
        num.append(line.strip().split())


def isprime(n):
    div = 2
    while div != n//2:
        div += 1
        if n%div == 0:
            return False
    return True

count = 0
for x in num:
    if isprime(int(x[0])):
        count += 1
print(count)

def dzielniki(n):
    div = 2
    dziel = []
    while div <= n//2 +1:
        if n%div == 0:
            dziel.append(div)
        div += 1
    return dziel

def dziel(num):
    dziel = dzielniki(int(num[0]))
    dziely = dzielniki(int(num[1]))
    for y in dziel:
        if y in dziely:
            return False
    return True

count = 0
for x in num:
    if dziel(x):
        count += 1
print(count)

count = 0
for i, n in enumerate(num):
    works = False
    for x in range(0, int(n[0])):
        if isprime(int(n[1])**x):
            if int(n[1])**x % int(n[0]) == int(n[2]):
                works = True
    if works:
        count += 1
    print(i,len(num))
print(count)



