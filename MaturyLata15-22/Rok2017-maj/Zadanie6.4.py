F = open("dane.txt")
Dane = []

for line in F:
    Dane.append(line.split())

dlugoscmax = 0

for j in range(len(Dane[0])):
    dlugosc = 1
    for z in range(len(Dane)-1):
        if Dane[z][j] == Dane[z+1][j]:
            dlugosc += 1
            if dlugosc > dlugoscmax:
                dlugoscmax = dlugosc
        else:
            dlugosc = 1
print(dlugoscmax)
