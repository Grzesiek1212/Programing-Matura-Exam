F = open("liczby.txt")

Liczby = []

for line in F:
    Liczby.append(line.rstrip())

ilosc = 0

for liczba in Liczby:
    if liczba[-1] == '4':
        czyPrawda = True
        for i in range(len(liczba)):
            if liczba[i] == '0':
                czyPrawda = False
                continue
        if czyPrawda == True:
            ilosc += 1

print(ilosc)