F = open("sygnaly.txt")

Sygnaly = []

for line in F:
    Sygnaly.append(line.rstrip())

dlugosc_maks = 0
slowonaj = ''
for slowo in Sygnaly:
    litery = list(set(slowo))
    if len(litery) > dlugosc_maks:
        dlugosc_maks = len(litery)
        slowonaj = slowo

    # if len(litery) == 26:
    #     print(slowonaj)


print(slowonaj, dlugosc_maks)