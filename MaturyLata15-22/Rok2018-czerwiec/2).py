F = open("dane1.txt")
G = open("dane2.txt")

Dane1 = []
Dane2 = []

for line in F:
    Dane1.append(line.split())

for lol in G:
    Dane2.append(lol.split())

ilosc = 0

for i in range(len(Dane1)):
    iloscP1 = 0
    iloscN1 = 0
    iloscP2 = 0
    iloscN2 = 0

    for j in range(len(Dane1[i])):
        if int(Dane1[i][j]) % 2 == 0:
            iloscP1 += 1
        if int(Dane1[i][j]) % 2 == 1:
            iloscN1 += 1
        if int(Dane2[i][j]) % 2 == 0:
            iloscP2 += 1
        if int(Dane2[i][j]) % 2 == 1:
            iloscN2 += 1
    if iloscP1 == iloscP2 == iloscN1 == iloscN2 == 5:
        ilosc += 1

print(ilosc)


