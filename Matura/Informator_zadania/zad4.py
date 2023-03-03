with open("DANE/dane4.txt") as f:
    ls = [int(x.strip()) for x in f]

res = [0, 0]
for i, num in enumerate(ls):
    count = 0
    for x in range(i):
        if num > ls[x]:
            count += 1
    if count > res[1]:
        res[1] = count
        res[0] = i

print(res)