with open("Dane/pary.txt") as f:
    ls = [x.strip() for x in f]

def isprime(num):
    div = 2
    while div != num:
        if num % div == 0:
            return False
        div += 1
    return True

primes = []
for num in range(2, 100):
    if isprime(num):
        primes.append(num)

#1
for row in ls:
    num = int(row.split()[0])
    if num % 2 == 0:
        solution = 0
        for prime in primes:
            if num - prime in primes and num - prime > solution:
                solution = num - prime
        print(num, num - solution, solution)

#2
for row in ls:
    word = row.split()[1]
    longest_letter = [1, word[0]] #[length, letter]
    current_length = 1
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            current_length += 1
            if current_length > longest_letter[0]:
                longest_letter = [current_length, word[i]]
        else:
            current_length = 1
    print(longest_letter[1]*longest_letter[0], longest_letter[0])

#3
solution = [99999, 'zzzzzzzzzzzzzzzzzzzzzzz']
for row in ls:
    row = row.split()
    row[0] = int(row[0])
    if row[0] == len(row[1]):
        if row[0] < solution[0] or (row[0] == solution[0] and row[1] < solution[1]):
            solution = row
print(solution)
