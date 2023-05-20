st = "[ [ ] [ ] [ [ [ ] [ ] ] [ ] ] ]"

a, b = 0, 0
for letter in st:
    if letter == "[":
        a += 1
    elif letter == "]":
        b += 1

print(a, b)