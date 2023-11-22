F = open("dane.txt")
Dane = []

for line in F:
    Dane.append(line.split())

ilosc = 0

for i in range(len(Dane)):
    licznik = 0
    for j in range(len(Dane[i])//2):
        if Dane[i][j] == Dane[i][-j-1]:
            licznik += 1

    if licznik != len(Dane[i])//2:
        ilosc += 1

print(ilosc)
