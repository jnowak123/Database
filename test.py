w = 0
n = 11111
while n != 0:
    w = w + n%10
    print(w)
    n = n // 10

print(w)