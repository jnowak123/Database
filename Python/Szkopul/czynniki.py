def primelist():
    square = 10 ** 6
    numlist = [True] * (square + 1)
    numlist[0] = False
    numlist[1] = False
    count = 2

    while count < square:
        if numlist[count]:
            remove = count * 2
            while remove <= square:
                if numlist[remove]:
                    numlist[remove] = False
                remove += count
        count += 1
    return [i for i in range(len(numlist)) if numlist[i]]

def prime_factors(i):
    x = 0
    while i != 1:
        try:
            if i % primes[x] == 0:
                print('{} | {}'.format(i, primes[x]))
                i = i // primes[x]
            else:
                x += 1
        except IndexError:
            print('{} | {}'.format(i, i))
            i = 1
    print('1 | -\n')

primes = primelist()
num = int(input())
for a in range(num):
    prime_factors(int(input()))