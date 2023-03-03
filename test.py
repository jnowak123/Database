def nwd(a, b):
    div = 0
    if a > b:
        div = b
    else:
        div = a
    while a%div != 0 or b%div != 0:
        div -= 1
    return div

print(nwd(90, 70))
