F = open("liczby.txt")

Liczby = []

for line in F:
    Liczby.append(line.rstrip())

ilosc = 0

for liczba in Liczby:
    if liczba[-2:] == '02':
        ilosc += 1

print(ilosc)