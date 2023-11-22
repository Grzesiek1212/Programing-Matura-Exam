F = open("galerie.txt")

Dane = []

for line in F:
    Dane.append(line.split())

najwieksza = 0
naj = ''

najm = ''
najmniejsza = 64



for galeria in Dane:
    sklepy = []
    for i in range(2,len(galeria),2):
        sklepy.append(int(galeria[i])*int(galeria[i+1]))
    j = 0
    while j < len(sklepy):
        if sklepy[j] == 0:
            sklepy.pop(j)
        else:
            j += 1

    rodzaje = list(set(sklepy))

    if len(rodzaje) > najwieksza:
        naj = galeria[1]
        najwieksza = len(rodzaje)

    if len(rodzaje) < najmniejsza:
        najm = galeria[1]
        najmniejsza = len(rodzaje)

print(naj, najwieksza)
print(najm, najmniejsza)




