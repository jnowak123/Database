people = int(input())
mylist = []

for a in range(people):
    x = list(map(int, input().split()))
    mylist.append(sum(x[1:len(x)]))

print(*mylist, sep="\n")