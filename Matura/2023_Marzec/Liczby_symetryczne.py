import math

with open("DANE/symetryczne.txt") as f:
    nums = [line.strip().split() for line in f]

def symetryczne(num):
    return True if num == num[::-1] and len(num) > 1 else False

res = 0
for line in nums:
    if symetryczne(line[1]):
        res += 1
print(res)

def polsymetryczne(num):
    for mid in range(2, len(num) -2):
        if int(num[0:mid]) >= 10 and int(num[mid:]) >= 10:
            if symetryczne(num[0:mid]) and symetryczne(num[mid:]):
                return True
    return False

nums_base10 = [int(line[1], int(line[0])) for line in nums]
res = 0
for line in nums_base10:
    if polsymetryczne(str(line)):
        res += 1
print(res)

nmax = [0, 0] # index, length
nums_base2 = [str(bin(x))[2:] for x in nums_base10]
for i, num in enumerate(nums_base2):
    if symetryczne(num):
        if len(num) > nmax[1]:
            nmax = [i, len(num)]
print(nums_base10[nmax[0]], nums[nmax[0]], nums_base2[nmax[0]])

def isprime(num):
    for div in range(2, round(math.sqrt(num)) +1):
        if num % div == 0:
            return False
    return True

res = 0
for num in nums_base10:
    if isprime(num) and symetryczne(str(num)):
        res += 1
print(res)



