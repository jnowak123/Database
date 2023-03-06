with open("DANE/dane1.txt") as f:
    ls1 = [list(map(int, x.strip().split(" "))) for x in f]
    

with open("DANE/dane2.txt") as f:
    ls2 = [list(map(int, x.strip().split(" "))) for x in f]

res = 0
for i in range(len(ls1)):
    if ls1[i][-1] == ls2[i][-1]:
        res += 1
print(res)

res = 0
for i in range(len(ls1)):

    odd, even, ls1_type = 0, 0, False
    for num in ls1[i]:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == odd:
        ls1_type = True

    odd, even, ls2_type = 0, 0, False
    for num in ls2[i]:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == odd:
        ls2_type = True

    if ls1_type and ls2_type:
        res += 1
print(res)

res = []
for i in range(len(ls1)):
    pair_type = True
    for num in ls2[i]:
        if num not in ls1[i]:
            pair_type = False
    if pair_type:
        res.append(i+1)
print(len(res), res)

str_res = ""
for i in range(len(ls1)):
    res = []
    i1, i2 = 0, 0

    while i1 < 10 and i2 < 10:
        if ls1[i][i1] <= ls2[i][i2]:
            res.append(ls1[i][i1])
            i1 += 1
        else:
            res.append(ls2[i][i2])
            i2 += 1

    if i1 == 9:
        for num in range(i2, 10):
            res.append(ls2[i][num])
    else:
        for num in range(i1, 10):
            res.append(ls1[i][num])
    str_res += str(res) + "\n"


with open("Wyniki/wynik4_4.txt", "w") as f:
    f.write(str(str_res))
