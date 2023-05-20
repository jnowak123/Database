alf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
with open("DANE/szyfrogram.txt") as f:
    f = [x.strip() for x in f]

alf_count = {letter:0 for letter in alf}
for word in f:
    for letter in word:
        alf_count[letter] += 1
print(alf_count)

with open("DANE/czestosc.txt") as g:
    g = [x.strip().split() for x in g]
    g = {int(x[1]):x[0] for x in g}

code = {letter:g[alf_count[letter]] for letter in alf}

key = "CAIMURJH"
ans = ""
for letter in key:
    ans += code[letter]
print(ans)

for word in f:
    ans = ""
    for letter in word:
        ans += code[letter]
    print(ans)