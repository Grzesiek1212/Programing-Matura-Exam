F = open("galerie.txt")

Dane = []

for line in F:
    Dane.append(line.split())

Kraje = []
for i in range(len(Dane)):
    Kraje.append(Dane[i][0])

Kraje1 = list(sorted(set(Kraje)))

for kraj in Kraje1:
    ilosc = 0
    for i in range(len(Kraje)):
        if kraj == Kraje[i]:
            ilosc += 1

    print(kraj, ilosc)
