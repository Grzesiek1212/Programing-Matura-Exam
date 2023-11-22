F = open("binarne.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def TwoToDec(x):
    liczba10 = 0
    for i in range(len(x)):
        liczba10 += int(x[i]) * 2**(len(x)-i-1)

    return liczba10

ilosc = 0
dlugoscmin = len(Dane[0])

for liczba in Dane:
    dlugosc = len(liczba)
    i = 0
    while i < dlugosc:
        if TwoToDec(liczba[i:i+4]) > 9:
            ilosc += 1
            if dlugosc < dlugoscmin:
                dlugoscmin = dlugosc
            break
        i += 4

print(ilosc)
print(dlugoscmin)


