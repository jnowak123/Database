def move_zeros(lst):
    return [x for x in lst if x != 0] + [0 for x in range(lst.count(0))]

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))