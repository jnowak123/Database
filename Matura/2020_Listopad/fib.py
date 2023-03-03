fib = [1, 1]
alf = list("ABCDEFGHIJLKMNOPQRSTUVWXYZ")
alf_dict= {}

for i in range(100):
    fib.append(fib[i] + fib[i+1])

for i, letter in enumerate(alf):
    alf_dict[i+1] = letter

print(alf_dict)
print(fib)

def zaszyfr(word):
    sol = []
    for i, letter in enumerate(word):
        for j in alf_dict:
            if alf_dict[j] == letter:
                x = j
        g = (x+(fib[i]%26))%26
        sol.append(alf_dict[g])
    return sol

print(zaszyfr("JANKOWALSKIPOZDRAWIA"))

