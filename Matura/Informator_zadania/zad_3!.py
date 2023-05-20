with open("DANE/dane3.txt") as f:
    f = [list(map(int, x.strip().split())) for x in f]

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


#unfinished
m = [[] for x in range(len(f))]
for i, line in enumerate(f):
    for i_b, line_b in enumerate(f):
        if line[0] <= line_b[0] and line[1] >= line_b[1] and i != i_b:
            m[i].append(i_b)
anslist = [-1 for x in range(len(f))]

def res(i, depth):
    if anslist[i] == -1:
        maxdepth = [res(x, depth +1) for x in m[i]]
        if maxdepth:
            print(type(max(maxdepth)))
            anslist[i] = depth - max(maxdepth)
            return max(maxdepth)
        else:
            anslist[i] = 0
            return maxdepth
    else:
        return anslist[i]

print(res(0, 0))
        