import random
nums = [random.randint(1, 100) for x in range(20)]


def sort(ls, i):
    while i > 0 and ls[i] < ls[i-1]:
        x = ls[i]
        ls[i] = ls[i-1]
        ls[i-1] = x
        i -= 1
    return ls

print(nums)
for i in range(1, 20):
    nums = sort(nums, i)
print(nums)