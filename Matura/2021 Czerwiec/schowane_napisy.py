ls = []
with open('DANE/przyklad.txt') as f:
    for line in f:
        ls.append(line.strip())

count = 0 
for line in ls:
    count += sum(l.isdigit() for l in line)
print(count)