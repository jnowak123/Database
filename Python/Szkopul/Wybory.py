num = int(input())
people = input().split()

leader = people[0]
record = 0

for a in range(num):
    if leader == people[a]:
        record += 1
    else:
        record -= 1
        if record < 0:
            record = 1
            leader = people[a]

if people.count(leader) > num/2:
    print(leader)
else:
    print('BRAK')
