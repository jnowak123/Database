with open('Dane/instrukcje.txt') as f:
    instructions = [x.split() for x in f]

word = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A']
for instruction in instructions:
    if instruction[0] == 'DOPISZ':
        word.append(instruction[1])
    elif instruction[0] == 'ZMIEN':
        word[-1] = instruction[1]
    elif instruction[0] == 'USUN':
        word.pop()
    else:
        for i, letter in enumerate(word):
            if letter == instruction[1]:
                word[i] = alphabet[alphabet.index(instruction[1]) +1]
                break

#1
print(len(word))

#2
sol = [0, 0]
count = 0
for i in range(len(instructions) -1):
    if instructions[i][0] == instructions[i+1][0]:
        count += 1
        if count > sol[1]:
            sol[0] = instructions[i][0]
            sol[1] = count
    else:
        count = 0
print(sol[0], sol[1] +1)

#3
letter_count = {}
for instruction in instructions:
    if instruction[0] == 'DOPISZ':
        if instruction[1] in letter_count:
            letter_count[instruction[1]] += 1
        else:
            letter_count[instruction[1]] = 1
sol = [0, 0]
for letter in letter_count:
    if letter_count[letter] > sol[1]:
        sol[0] = letter
        sol[1] = letter_count[letter]
print(sol)

#4
print("".join(word))