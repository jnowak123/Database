with open('DANE/genetyka.txt') as f:
    kombinacje = [x.strip() for x in f]

mutacje = {
    "BD" : "A",
    "CA" : "B",
    "CD" : "B",
    "DD" : "C",
    "BC" : "D"}

def mutate(gene):
    sol = []
    for x in range(0, len(gene), 2):
        if gene[x:x+2] in mutacje:
            sol.append(mutacje[gene[x:x+2]])
        else:
            return False
    return "".join(sol)

def rewind(gene):
    while len(gene) != 1:
        gene = mutate(gene)
        if gene == False:
            return False
    return True

ans = 0
for kombinacja in kombinacje:
    if not rewind(kombinacja):
        ans += 1
print(ans, len(kombinacje))
