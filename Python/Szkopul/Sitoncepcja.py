import math
brak = True
name = 2


def isprime(num):
    numlist = [True]*(num+1)
    numlist[0] = False
    numlist[1] = False
    count = 2
    square = math.sqrt(num)
    returnlist = []

    while count < square:
        returncount = 0
        if numlist[count]:
            remove = count*2
            while remove <= num:
                if numlist[remove]:
                    numlist[remove] = False
                    returncount += 1
                remove += count
        returnlist.append(returncount)
        count += 1
    return numlist, returnlist


numlist, returnlist = isprime(int(input()))

for a in returnlist:
    if numlist[a]:
        print(name, a)
        brak = False
    name += 1

if brak:
    print('BRAK')