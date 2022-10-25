arr = [784, 4765, 5291]

#arr = input().strip()
changes = 8
for i in range(3):
    arr[i] = list(map(int, list(str(arr[i]))))
    rem = 3 - sum(int(x) for x in arr[i])%3
    changes -= rem
    arr[i][0] += rem
    arr[i] = int(''.join(map(str, arr[i])))

if changes >= 3:
    max = [0, 0]
    for i in range(3):
        if arr[i] >= max[0]:
            max[0] = arr[i]
            max[1] = i
    arr[max[1]] = list(map(int, list(str(arr[i]))))
    arr[max[1]][0] += changes - changes%3
    print(arr)
    arr[max[1]] = int(''.join(map(str, arr[i])))

print(arr)



