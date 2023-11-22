F = open("dane4.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())


najmniejsza = abs(int(Dane[0]) - int(Dane[1]))
najwieksza = 0

for i in range(len(Dane)-1):
    luka = abs(int(Dane[i]) - int(Dane[i+1]))
    if luka > najwieksza:
            najwieksza = luka
    if luka < najmniejsza:
            najmniejsza = luka

print(najwieksza, najmniejsza)

