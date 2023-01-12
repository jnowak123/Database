with open('Dane/Galerie.txt') as f:
    galerie = [x.strip().split() for x in f]

#1
kraje = {}
for galeria in galerie:
    if galeria[0] in kraje:
        kraje[galeria[0]] += 1
    else:
        kraje[galeria[0]] = 1
print(kraje)

#2 a
sol = {}
for galeria in galerie:
    count = [0, 0] #powierzchnia, liczba lokali
    for i in range(2, 140, 2):
        galeria[i] = int(galeria[i])
        galeria[i +1] = int(galeria[i +1])
        if galeria[i] == 0:
            break
        count[0] += galeria[i]*galeria[i+1]
        count[1] += 1
    sol[galeria[1]] = count
print(sol)
#b
max = [0, 0]
min = [0, 99999999]
for galeria in sol:
    if sol[galeria][0] > max[1]:
        max[0] = galeria
        max[1] = sol[galeria][0]
    if sol[galeria][0] < min[1]:
        min[0] = galeria
        min[1] = sol[galeria][0]
print(max, min)

#3
max = [0, 0]
min = [0, 999999999]
for galeria in galerie:
    typy = []
    for i in range(2, 140, 2):
        galeria[i] = int(galeria[i])
        galeria[i +1] = int(galeria[i +1])
        powierzchnia = galeria[i]*galeria[i+1]
        if powierzchnia not in typy and powierzchnia != 0:
            typy.append(powierzchnia)
    if len(typy) > max[1]:
        max[0] = galeria[1]
        max[1] = len(typy)
    if len(typy) < min[1]:
        min[0] = galeria[1]
        min[1] = len(typy)
print(max, min)