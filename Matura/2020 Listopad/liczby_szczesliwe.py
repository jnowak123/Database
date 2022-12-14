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

count = 1
while lucky_nums[-1] != lucky_nums[count]:
    count += 1
    lucky_nums = remove_nums(lucky_nums, lucky_nums[count])

print(lucky_nums)



