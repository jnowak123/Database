with open('DANE/sygnaly.txt') as f:
    ls = [x.strip() for x in f]

sol = []
for i in range(39, 1000, 40):
    sol.append(ls[i][9])
print("".join(sol))

sol = [0, 0]
for row in ls:
    letters = []
    for letter in row:
        if letter not in letters:
            letters.append(letter)
    x = len(letters)
    if x > sol[1]:
        sol = [row, x]
print(sol)

with open('DANE/sygnaly.txt') as f:
    ls = [x.strip() for x in f]

a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphabet = {}
for i, letter in enumerate(a):
    alphabet[letter] = i +1

sol = []
for row in ls:
    x = True
    for letter in row:
        for letter2 in row:
            if abs(alphabet[letter] - alphabet[letter2]) > 10:
                x = False
    if x == True:
        sol.append(row)
for line in sol:
    print(line)

print(abs(alphabet["A"] - alphabet["A"]))
