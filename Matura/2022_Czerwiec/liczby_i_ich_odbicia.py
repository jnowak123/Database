liczby = []
with open('dane/liczby.txt') as f:
    [liczby.append(liczba.strip()) for liczba in f]

for liczba in liczby:
    if int(liczba[::-1]) % 17 == 0:
        print(liczba[::-1])

max = [0, 0]
for liczba in liczby:
    if abs(int(liczba) - int(liczba[::-1])) > max[1]:
        max[1] = abs(int(liczba) - int(liczba[::-1]))
        max[0] = liczba
print(max)

def isprime(num):
    div = 2
    while div != num:
        if num % div == 0:
            return False
        div += 1
    return True

for liczba in liczby:
    if isprime(int(liczba)) and isprime(int(liczba[::-1])):
        print(liczba)

dic = {}
for liczba in liczby:
    if liczba in dic:
        dic[liczba] += 1
    else:
        dic[liczba] = 0

count = [0,0,0]
for liczba in dic:
    count[dic[liczba]] += 1
count[0] += count[1] + count[2]

print(count)
