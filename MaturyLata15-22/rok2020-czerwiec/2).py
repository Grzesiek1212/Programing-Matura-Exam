F = open("pary.txt")

Dane = []
Dane_2 =[]
for line in F:
    Dane.append(line.split())

for i in range(len(Dane)):
    Dane_2.append(Dane[i][1])

def najdlszy(x):
    naj = 0
    dlugosc = 1
    index = 0
    for i in range(1,len(x)):
        if x[i] == x[i-1]:
            dlugosc += 1
            if dlugosc > naj:
                naj = dlugosc
                index = i
        else:
            dlugosc = 1

    if naj == 0:
        return x[0]
    else:
        return x[index-naj+1:index+1]

for slowo in Dane_2:
    print(najdlszy(slowo), len(najdlszy(slowo)))

