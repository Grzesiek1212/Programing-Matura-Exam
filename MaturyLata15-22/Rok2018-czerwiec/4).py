F = open("dane1.txt")
G = open("dane2.txt")
W = open('wynik4_4.txt', 'w')

Dane1 = []
Dane2 = []

for line in F:
    Dane1.append(line.split())

for lol in G:
    Dane2.append(lol.split())

for i in range(len(Dane1)):
    j = 0
    l = 0
    ciag = ''
    while l <= 9 and j <= 9:
        if int(Dane1[i][j]) <= int(Dane2[i][l]):
            ciag += " " + Dane1[i][j]
            j += 1
        else:
            ciag += " " + Dane2[i][l]
            l += 1

    if l > j:
        for s in range(j,10):
            ciag += " " + Dane1[i][s]
    else:
        for m in range(l, 10):
            ciag += " " + Dane2[i][m]

    W.write(f'{ciag[1:]}\n')

F.close()
G.close()
W.close()

