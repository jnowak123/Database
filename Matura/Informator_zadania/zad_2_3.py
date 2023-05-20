with open("DANE/dane2_3.txt") as f:
    f = [x.strip() for x in f]


for line in f:
    ans = 0
    depth = 0
    for char in line:
        if char == "[":
            depth += 1
        else:
            depth -= 1
        if depth > ans:
            ans = depth
    print(ans)
