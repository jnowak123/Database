with open("DANE_PR/odszyfruj.txt") as f:
    text = [x.strip() for x in f]

a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alf = {}
for i, letter in enumerate(a):
    alf[letter] = i +1

for i in range(0, len(text), 2):
    jawny = text[i]
    zaszyfr = text[i+1]
    odp = []
    for i, letter in enumerate(jawny):
        if letter != " ":
            odp.append(a[(alf[zaszyfr[i]] - alf[letter]) -1])
    print("".join(odp))

