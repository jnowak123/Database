def to_basex(num, base):
    res = []
    div = base
    while div <= num:
        div = div * base
    while div != 0:
        res.append(num // div)
        num = num % div
        div = round(div / base)
    return res[1:]

def to_base10(num, base):
    res = 0
    l = len(str(num)) -1
    for num in str(num):
        res += (base ** l)*int(num)
        l -= 1
    return res

print(to_base10(576284, 9))
