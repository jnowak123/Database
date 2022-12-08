ls = []
with open('DANE/napisy.txt') as f:
    for line in f:
        ls.append(line.strip())

count = 0 
for line in ls:
    count += sum(l.isdigit() for l in line)
print(count)

ans =[]
for x in range(50):
    ans.append(ls[((x+1)*20) -1][x])
print(''.join(ans))

ans =[]
for line in ls:
    odwl = line[::-1]
    if line[1::] == line[:0:-1]:
        ans.append(line[25])
    elif line[:-1] == odwl[1::]:
        ans.append(line[24])
print(ans)

def cztery(ls):
    ans = []
    for line in ls:
        num = []
        for letter in list(line):
            if letter.isdigit():
                num.append(letter)
            if len(num) == 2:
                num = int(''.join(num))
                if num >=65 and num <=90:
                    ans.append(chr(num))
                    if ans[:-4:-1] == ['X', 'X', 'X']:
                        return ans
                num = []
                
print(cztery(ls))