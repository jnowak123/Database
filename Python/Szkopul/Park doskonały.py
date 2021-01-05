type = input().strip()
amount = int(input())
trees = []
for a in range(amount):
    trees.append(list(map(int, input().split())))
count = 0

if type == 'WERTYKALNY':
    for a in trees:
        if [-a[0], a[1]] in trees:
            count += 1
elif type == 'HORYZONTALNY':
    for a in trees:
        if [a[0], -a[1]] in trees:
            count += 1
else:
    for a in trees:
        if [-a[0], -a[1]] in trees:
            count += 1

if count == len(trees):
    print('TAK')
else:
    print('NIE')