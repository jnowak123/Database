with open("DANE/dane3.txt") as f:
    f = [list(map(int, x.strip().split())) for x in f]
    n = len(f)

ans = [999999, 0]
for line in f:
    l = line[1] - line[0] +1
    if l < ans[0]:
        ans[1] = ans[0]
        ans[0] = l

print(ans)

distances = [0 for x in range(2024*2)]
for line in f:
    distances[line[1] - line[0] +1] += 1

for i in range(len(distances)-1, 0, -1):
    if distances[i] == max(distances):
        print(i)
        break

depth = [-1 for x in range(n)]
        
def rec(i):
    if depth[i] != -1:
        return depth[i]
    max_depth = 0
    for j in range(n):
        if j != i and f[i][0] < f[j][0] and f[i][1] > f[j][1]:
            x = rec(j)
            if x > max_depth:
                max_depth = x
    depth[i] = max_depth +1
    return max_depth +1

for i in range(n):
    rec(i)

print(max(depth))
