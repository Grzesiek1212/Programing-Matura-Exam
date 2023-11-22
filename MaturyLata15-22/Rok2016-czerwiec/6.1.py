F = open("liczby.txt")

Liczby = []

for line in F:
    Liczby.append(line.rstrip())

ilosc = 0
for liczba in Liczby:
    if liczba[-1] == '8':
        ilosc += 1

print(ilosc)