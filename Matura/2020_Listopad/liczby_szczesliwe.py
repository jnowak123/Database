with open("dane/dane.txt") as f:
    nums = [x.strip() for x in f]

lucky_nums = [x +1 for x in range(0, 10000, 2)]

def remove_nums(ls, x):
    ans, count = [], 0
    for num in ls:
        count += 1
        if count == x:
            count = 0
        else:
            ans.append(num)
    return(ans)

num = 1
while lucky_nums[-1] != lucky_nums[num]:
    num += 1
    lucky_nums = remove_nums(lucky_nums, lucky_nums[num])

print(lucky_nums)



