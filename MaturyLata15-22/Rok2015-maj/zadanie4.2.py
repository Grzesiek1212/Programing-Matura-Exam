F = open("liczby.txt")
Liczby = []

for line in F:
    Liczby.append(line.rstrip())


podzilene2 = 0
podzielne8 = 0

for liczba in Liczby:
    if liczba[-1] == '0':
        podzilene2 += 1

    if liczba[-3:] == '000':
        podzielne8 += 1

print(podzilene2)
print(podzielne8)
