F = open("instrukcje.txt")

Dane = []

for line in F:
    Dane.append(line.split())


Napis = ''

D = "DOPISZ"
Z = "ZMIEN"
U = "USUN"
P = "PRZESUN"

for i  in range(len(Dane)):
    if Dane[i][0] == D:
        Napis += Dane[i][1]

    if Dane[i][0] == Z:
        Napis = Napis[:-1]
        Napis += Dane[i][1]

    if Dane[i][0] == U:
        Napis = Napis[:-1]

    if Dane[i][0] == P:
        j = Napis.index(str(Dane[i][1]))
        if ord(Dane[i][1])+1 > 90:
            Napis = Napis[:j] + chr(ord(Dane[i][1])+1-26) + Napis[j+1:]
        else:
            Napis = Napis[:j] + chr(ord(Dane[i][1]) + 1) + Napis[j + 1:]

print(Napis)