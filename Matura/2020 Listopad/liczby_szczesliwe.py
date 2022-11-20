with open("dane/dane.txt") as f:
    nums = [x.strip() for x in f]

lucky_nums = [1 for x in range(10000)]
print(lucky_nums)
