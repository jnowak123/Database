with open("DANE/dane.txt") as f:
    nums = [int(x.strip()) for x in f]

fib = [0, 1]
while fib[-1] < 1000000000:
    fib.append(fib[-1] + fib[-2])

fib_nums = []
for num in nums:
    if num in fib:
        fib_nums.append(num)
print(fib_nums)

print(max(fib_nums), min(fib_nums))

res = 0
count = 0
for i in range(1, len(nums)):
    if nums[i-1] < nums[i]:
        count += 1
        if count > res:
            res = count
    else:
        count = 0
print(res)