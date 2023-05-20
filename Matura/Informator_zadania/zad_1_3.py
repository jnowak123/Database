with open("DANE/dane1_3.txt") as f:
    nums = [int(x.strip()) for x in f]

n = len(nums)
ans = 0

for beg in range(0, n):
    for end in range(beg, n):
        s = sum(nums[beg:end])
        if s > ans:
            ans = s

print(ans)