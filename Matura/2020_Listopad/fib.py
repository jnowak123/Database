alf_list = list("ABCDEFGHIJKLLMNOPQRSTUVWXYZ")
alf = {letter : i for i, letter in enumerate(alf_list)}

fib = [1, 1]
for i in range(100):
    fib.append(fib[i] + fib[i+1])
fib = [x % 26 for x in fib]

def szyfr(word):
    sol = []
    for i, letter in enumerate(word):
        sol.append(alf_list[(alf[letter] + fib[i]) %26])
    return sol

print(szyfr("JANKOWALSKIPOZDRAWIA"))

