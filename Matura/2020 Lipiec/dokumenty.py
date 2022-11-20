with open('DANE/identyfikator_przyklad.txt') as f:
    identyfikatory = [x.strip() for x in f]

for i, identyfikator in enumerate(identyfikatory):
    identyfikatory[i] = [identyfikator[0:3], identyfikator[3:]]

#1
max = [0, []]
for identyfikator in identyfikatory:
    suma = sum(list(map(int, list(identyfikator[1]))))
    if suma > max[0]:
        max[0] = suma
        max[1] = [identyfikator]
    elif suma == max[0]:
        max[1].append(identyfikator)
print(max[1])

#2 
for identyfikator in identyfikatory:
    if identyfikator[1] == identyfikator[1][::-1] or identyfikator[0] == identyfikator[0][::-1]:
        print(identyfikator)

#3
alphabet = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
multiplier = [7, 3, 1, 0, 7, 3, 1, 7, 3]
for identyfikator in identyfikatory:
    suma = 0
    identyfikator = "".join(identyfikator)
    for i, letter in enumerate(identyfikator):
        if i in (0, 1, 2):
            suma += alphabet[letter] * multiplier[i]
        else:
            suma += int(letter) * multiplier[i]
    if suma % 10 != int(identyfikator[3]):
        print(identyfikator)