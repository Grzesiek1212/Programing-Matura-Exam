F = open("liczby.txt")

Liczby = []

for line in F:
    Liczby.append(line.rstrip())

def AnytoDec(liczba, system):
    liczba10 = 0
    for i in range(len(liczba)):
        liczba10 += int(liczba[i]) * system ** (len(liczba) - i - 1)
    return liczba10

kod_max = ''
kod_min = ''
wartosc_max = 0
wartosc_min = AnytoDec(Liczby[0][:-1], int(Liczby[0][-1]))
for liczba in Liczby:
    if AnytoDec(liczba[:-1], int(liczba[-1])) > wartosc_max:
        wartosc_max = AnytoDec(liczba[:-1], int(liczba[-1]))
        kod_max = liczba

    if AnytoDec(liczba[:-1], int(liczba[-1])) < wartosc_min:
        wartosc_min = AnytoDec(liczba[:-1], int(liczba[-1]))
        kod_min = liczba

print(kod_max, wartosc_max)
print(kod_min, wartosc_min)


