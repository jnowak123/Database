info = list(map(int, input().split()))
add = info[0] % (info[1] + info[2])

if add - info[1] < 0:
    print(1)
else:
    print(0)