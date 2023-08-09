def dig_pow(n, p):
    s = sum(num**(pow+p) for pow, num in enumerate(list(map(int, list(str(n))))))
    return s // n if s%n == 0 else -1

print(dig_pow(46288, 3))