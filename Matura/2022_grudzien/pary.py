with open("DANE/pary.txt") as f:
    pairs = [list(map(int, x.strip().split())) for x in f]

def draw(num, ans, max):
    if num *2 <= max:
        if num*2 == ans:
            return num, ans
        res = draw(num*2, ans, max)
        if res != None:
            return res
    if (num *2) +1 <= max:
        if (num *2) +1 == ans:
            return num, ans
        res = draw((num *2) +1, ans, max)
        if res != None:
            return res

ans = []
for pair in pairs:
    res = draw(pair[0], pair[1], 100000)
    if res != None:
        ans.append(pair)

print(ans)

