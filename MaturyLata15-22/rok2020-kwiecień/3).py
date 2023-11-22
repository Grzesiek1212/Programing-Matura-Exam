F = open("dane4.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

Luki = []
Krotnosci = [0]

for j in range(len(Dane) - 1):
    luka = abs(int(Dane[j]) - int(Dane[j + 1]))
    Luki.append(luka)

Luki_moz = []

Luki_moz = list(sorted(set(Luki)))
Ile = []

for i in range(len(Luki_moz)):
    Ile.append(Luki.count(Luki_moz[i]))

Najczestsza = max(Ile)

for i in range(len(Luki_moz)):
    if Ile[i] == Najczestsza:
        print(Najczestsza, Luki_moz[i])
