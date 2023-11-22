F = open("binarne.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

ilosc = 0
maksdlugosc = 0
napis = ''

for liczba in Dane:
    dlugosc = len(liczba)
    if liczba[:dlugosc//2] == liczba[dlugosc//2:]:
        ilosc += 1
        if dlugosc > maksdlugosc:
            maksdlugosc = dlugosc
            napis = liczba

print(ilosc)
print(maksdlugosc, napis)