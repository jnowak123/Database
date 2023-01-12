with open("DANE/dane4.txt") as f:
    nums = [int(x.strip()) for x in f]

differences = []
for i in range(len(nums) -1):
    differences.append(abs(nums[i] - nums[i+1]))

print(max(differences), min(differences))

