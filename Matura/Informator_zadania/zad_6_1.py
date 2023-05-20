with open("DANE/dane6.txt") as f:
    f = [x.strip() for x in f]

for p in range(2, 11):
    count = 0
    
    for num in f:
        isnum = False
        if str(p-1) in num:
            isnum = True
            for char in num:
                if int(char) > p-1:
                    isnum = False
        if isnum:
            count += 1

    print(p, count)

for p in range(2, 11):
    maxsum = [0, 0]
    
    for num in f:
        isnum = False
        if str(p-1) in num:
            isnum = True
            for char in num:
                if int(char) > p-1:
                    isnum = False
        if isnum:
            s = sum([int(x) for x in num])
            if s > maxsum[1]:
                maxsum = [num, s]

    print(p, maxsum)

for num in f:
    isnum = True
    for i in range(len(num)//2):
        if num[i] == num[len(num)-i-1]:
            isnum = False
    if isnum:
        print(num)