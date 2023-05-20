import math

with open('DANE/punkty.txt') as f:
    punkty = [list(map(int, x.strip().split())) for x in f][1:]

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p2[0])**2)

res = 0
for p1 in punkty:
    for p2 in punkty:
        for p3 in punkty:
            if distance(p1, p2)**2 + distance(p1, p3)**2 == distance(p2, p3)**2:
                res += 1

print(res)