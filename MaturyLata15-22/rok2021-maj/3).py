F = open("instrukcje.txt")

Dane = []

for line in F:
    Dane.append(line.split())

Dopisz = []

for i in range(len(Dane)):
    if Dane[i][0] == 'DOPISZ':
        Dopisz.append(Dane[i][1])

Mozliwosci = list(sorted(set(Dopisz)))
Ilosc =[]
for j in range(len(Mozliwosci)):
    ilosc = 0
    for z in range(len(Dopisz)):
        if Dopisz[z] == Mozliwosci[j]:
            ilosc += 1
    Ilosc.append(ilosc)

x = Ilosc.index(max(Ilosc))

print(Mozliwosci[x], max(Ilosc))