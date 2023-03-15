with open("DANE\dane.txt") as f:
    piksele = [list(map(int, line.split())) for line in f]

res = [0, 999]
for line in piksele:
    for number in line:
        if number > res[0]:
            res[0] = number
        if number < res[1]:
            res[1] = number
print(res)

res = 0
for line in piksele:
    if line != line[::-1]:
        res += 1
print(res)

res = 0
for x, line in enumerate(piksele):
    for y, number in enumerate(line):
        if x > 0 and abs(number - piksele[x-1][y]) > 128:
            res += 1
        elif x < 199 and abs(number - piksele[x+1][y]) > 128:
            res += 1
        elif y > 0 and abs(number - piksele[x][y-1]) > 128:
            res += 1
        elif y < 319 and abs(number - piksele[x][y+1]) > 128:
            res += 1
print(res)

res = 0
count = 1
for y in range(0, 320):
    for x in range(0, 199):
        if piksele[x][y] == piksele[x+1][y]:
            count += 1
        else:
            if count > res:
                res = count
            count = 1
print(res)
