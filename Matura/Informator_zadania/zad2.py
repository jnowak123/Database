with open("DANE/dane2_3.txt")as f:
    ls = [list(x.strip()) for x in f]

for line in ls:
    num = 0
    m = 0
    for x in line:
        if x == "[":
            num += 1
        else:
            num -= 1
        if num > m:
            m = num
    print(m)


with open("DANE/dane2_4.txt")as f:
    ls = [list(x.strip()) for x in f]

def test(line):
    if line[0] == "]":
        return False
    a, b = 0, 0
    for x in line:
        if x == "[":
            a += 1
        else:
            b += 1
    return a == b

for line in ls:
    print(test(line))




