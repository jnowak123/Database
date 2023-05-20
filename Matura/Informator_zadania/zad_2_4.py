with open("DANE/dane2_4.txt") as f:
    f = [x.strip() for x in f]

for line in f:
    a, b = 0, 0
    for char in line:
        if char == "[":
            a += 1
        elif char == "]":
            b += 1
    print(a==b)