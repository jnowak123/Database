from math import sqrt

with open("punkty.txt") as f:
    punkty = [list(map(int, x.strip().split())) for x in f]

def isprime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

count = 0
for line in punkty:
    if isprime(line[0]) and isprime(line[1]):
        count += 1
print(count)

def are_equal(line):
    for num in list(str(line[0])):
        if num not in str(line[1]):
            return False
    for num in list(str(line[1])):
        if num not in str(line[0]):
            return False
    return True

count = 0
for line in punkty:
    if are_equal(line):
        count += 1
print(count)

maxdis = 0
sol = []
for line1 in punkty:
    for line2 in punkty:
        dis = round(sqrt((line2[0] - line1[0])**2 + (line2[1] - line1[1])**2))
        if dis > maxdis:
            maxdis = dis
            sol = [line1, line2]
print(maxdis, sol)

sol = [0, 0, 0] # wewnątrz, na, na zewnątrz
for line in punkty:
    if line[0] < 5000 and line[1] < 5000:
        sol[0] += 1
    elif line[0] < 5000 and line[1] == 5000:
        sol[1] += 1
    elif line[0] == 5000 and line[1] < 5000:
        sol[1] += 1
    else:
        sol[2] += 1
print(sol)


