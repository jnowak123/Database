with open("DANE/liczby.txt") as f:
    nums = [int(x.strip()) for x in f]

count = 0
for num in nums:
    while num % 3 == 0:
        num = num /3
    if num == 1 or num == 0:
        count += 1
print("1.", count)

print("2 -------")
count = 0
for num in nums:
    x = 0
    num = str(num)
    for i in range(len(num)):
        silnia = 1
        for j in range(int(num[i])):
            silnia = silnia*(j+1)
        x += silnia
    num = int(num)
    if num == x:
        print(num)
print("-------")

def nwd(a, b):
    div = 0
    if a > b:
        div = b
    else:
        div = a
    while a%div != 0 or b%div != 0:
        div -= 1
    return div

div = nums[0]
current = [0, 0]
max = [0, 0, 0]
for i in range(len(nums)):
    cdiv = div
    div = nwd(div, nums[i])
    if div != 1:
        current[1] += 1
    else:
        if current[1] > max[1]:
            max = [nums[current[0]-1], current[1], cdiv]
        div = nums[i]
        current = [i, 1]

print(max)
