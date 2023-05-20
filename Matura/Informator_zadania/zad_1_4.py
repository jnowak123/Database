with open("DANE/dane1_4.txt") as f:
    nums = [int(x.strip()) for x in f]

beg = 0
x = nums[0]
ans = [0, 'beg', 'end']
for i in range(1, len(nums)):
    if x + nums[i] < nums[i]:
        x = nums[1]
        beg = i
    else:
        x += nums[i]
    if x > ans[0]:
        ans = [x, beg, i]

print(ans)

