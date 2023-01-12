import math
with open('DANE/liczby.txt') as f:
    nums = [int(x.strip()) for x in f]
n = 1000000

primes = [True for x in range(n+1)]
primes[0], primes[1] = False, False

for i in range(2, math.ceil(math.sqrt(n)) +1):
    if primes[i]:
        j = i*2
        while j < n:
            primes[j] = False
            j += i
primenums = []
for i, num in enumerate(primes):
    if num:
        primenums.append(i)

count = 0
for num in nums:
    if num-1 in primenums:
        count += 1
print(count)

maxnum = [0, 0]
minnum = [0, 99999999999]
count = 0
for num in nums:
    max = 0
    for i, x in enumerate(primenums):
        if x >= num:
            max = i
            break
    numcount = 0
    for x in range(0, max):
        if primes[num - primenums[x]]:
            numcount += 1
    if numcount > maxnum[1]:
        maxnum[0] = num
        maxnum[1] = numcount
    if numcount < minnum[1]:
        minnum[0] = num
        minnum[1] = numcount
    count += 1
maxnum[1] = math.ceil(maxnum[1]/2)
minnum[1] = math.ceil(minnum[1]/2)
print(maxnum, minnum)

with open('liczbydec.txt') as f:
    nums = [x.strip() for x in f]
dic = {}

for num in nums:
    for letter in num:
        try:
            dic[letter] += 1
        except:
            dic[letter] = 1
print(dic)