F = open("galerie.txt")

Dane = []

for line in F:
    Dane.append(line.split())


najwieksza = 0
naj = ''

najm = ''
najmniejsza = 3628
for galeria in Dane:
    sklepy = []
    for i in range(2,len(galeria),2):
        sklepy.append(int(galeria[i])*int(galeria[i+1]))

    ilosc = 0
    powierzchnia = sum(sklepy)

    for j in range(len(sklepy)):
        if sklepy[j] != 0:
            ilosc += 1

    if powierzchnia > najwieksza:
        naj = galeria[1]
        najwieksza = powierzchnia

    if powierzchnia < najmniejsza:
        najm = galeria[1]
        najmniejsza = powierzchnia

print(naj, najwieksza)
print(najm, najmniejsza)