F = open("liczby.txt")

Liczby = []

for line in F:
    Liczby.append(line.rstrip())

suma = 0

for liczba in Liczby:
    if liczba[-1] == '8':
        suma += int(liczba[:-1], 8)

print(suma)

