with open("DANE/dane4.txt") as f:
    f = [int(x.strip()) for x in f]

res = [0, 0]
for i in range(len(f)):
    count = 0
    for i_2 in range(0, i):
        if f[i] > f[i_2]:
            count += 1
    if count > res[1]:
        res = [i, count]

print(res[0] +1)