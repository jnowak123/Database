with open('liczby.txt') as file:
    numbers = [x.strip() for x in file]

#pierwsze
c = 0
for num in numbers:
    if num[0] == num[-1]:
        if c == 0:
            fnum = num
        c += 1   
odp1 = "Zadanie 4.1:", c, fnum

numbers = [int(num) for num in numbers]

#drugie
maxdiv = 0
maxcount = 0
for num in numbers:

    inum = int(num)
    div = 2
    divlist = []

    while inum != 1:
        if inum % div == 0:
            inum = inum/div
            divlist.append(div)
            div = 2
        else:
            div += 1
    
    if len(divlist) > maxdiv:
        maxdiv = len(divlist)
        maxdivnum = num

    count_list = []
    for div in divlist:
        if div not in count_list:
            count_list.append(div)
    if len(count_list) > maxcount:
        maxcount = len(count_list)
        maxcountnum = num

odp2 = "Zadanie 4.2:", maxdivnum, maxdiv, maxcountnum, maxcount

#trzecie
dic = {}
for div in numbers:
    dic[div] = []
    for num in numbers:
        if num % div == 0 and num != div:
            dic[div].append(num)

count = 0
for x in dic:
    for y in dic[x]:
        for z in dic[y]:
            count += 1
odp3 = count

count = 0
for a in dic:
    for b in dic[a]:
        for c in dic[b]:
            for d in dic[c]:
                for e in dic[d]:
                    count += 1
odp3 = "Zadanie 4.3:", odp3, count

print(odp1)
print(odp2)
print(odp3)



    

