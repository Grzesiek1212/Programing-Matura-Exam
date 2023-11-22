F = open("instrukcje.txt")

Dane = []

for line in F:
    Dane.append(line.split())


najdluzszy = 0
rodzaj = ''

for i in range(len(Dane)):
    ciag = 1
    for j in range(i+1, len(Dane)):
        if Dane[j][0] == Dane[i][0]:
            ciag += 1
            if ciag > najdluzszy:
                najdluzszy = ciag
                rodzaj = Dane[i][0]
        else:
            break

print(najdluzszy, rodzaj)
