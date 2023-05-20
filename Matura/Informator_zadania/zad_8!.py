with open("DANE/dane8.txt") as f:
    f = [int(x.strip()) for x in f]
    n = len(f)

ans = [0, 0]
for i in range(0, n -1):
    luka = abs(f[i] - f[i+1])
    if luka % 2 == 0:
        ans[0] += 1
    else:
        ans[1] += 1
print(ans)

ans = 0
for i in range(0, n -1):
    for j in range(i, n):
        if f[i] > f[j]:
            ans += 1
print(ans)

ans = 0
c = 1
for i in range(0, n -1):
    if f[i] < f[i+1]:
        c += 1
    else:
        if c > ans:
            ans = c
        c = 1
print(ans)

