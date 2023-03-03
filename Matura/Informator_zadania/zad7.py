with open("DANE/szyfrogram.txt") as f:
    szyfr = [row.strip() for row in f]

with open("DANE/czestosc.txt") as f:
    key = [row.strip().split() for row in f]

alfabet = {}

for row in szyfr:
    for letter in row:
        if letter not in alfabet:
            alfabet[letter] = 0
        alfabet[letter] += 1
print(alfabet)

trans = {}

for letter in key:
    for i in alfabet:
        if int(letter[1]) == alfabet[i]:
            trans[i] = letter[0]

word = "CAIMURJH"
sol = []
for letter in word:
    sol.append(trans[letter])
print(sol)

sol = []
for row in szyfr:
    rsol = []
    for letter in row:
        rsol.append(trans[letter])
    sol.append("".join(rsol))
print(sol)

