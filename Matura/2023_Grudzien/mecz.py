with open('DANE/mecz.txt') as f:
    file = [x for x in list(f)[0]]

count = 0
for i in range(len(file)-1):
    if file[i] != file[i+1]:
        count += 1
print(count)

def zad2(beg):
    result = [0, 0]
    for i in range(beg, len(file)):
        if file[i] == 'A':
            result[0] += 1
        else:
            result[1] += 1
        if result[0] >= 1000 and result[0] - result[1] >= 3:
            return result, i
        elif result[1] >= 1000 and result[1] - result[0] >= 3:
            return result, i
print(zad2(0)[0])

matches = [0]
while matches[-1] != len(file):
    res = zad2(matches[-1])
    if not res:
        break
    matches.append(res[1])
matches.append(10000)

matches[0] -= 1
matches[-1] -= 1
streaks = 0
maxstreak = ['X', 0]
for i in range(len(matches) -1):
    current = ['X', 0]
    for x in range(matches[i] +1, matches[i+1] +1):
        if file[x] == current[0]:
            current[1] += 1
        else:
            if current[1] >= 10:
                streaks += 1
                if current[1] > maxstreak[1]:
                    maxstreak[1] = current[1]
                    maxstreak[0] = current[0]
            current = [file[x], 1]
    if current[1] >= 10:
        streaks += 1
        if current[1] > maxstreak[1]:
            maxstreak[1] = current[1]
            maxstreak[0] = current[0]
print(streaks, maxstreak)




