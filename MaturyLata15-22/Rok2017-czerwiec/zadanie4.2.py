F = open("punkty.txt")

Dane = []

for line in F:
    Dane.append(line.split())

ilosc = 0

def Czycyfropodobne(x,y):
    CyfrX = []
    CyfrY = []

    for i in range(len(x)):
        CyfrX.append(x[i])

    for j in range(len(y)):
        CyfrY.append(y[j])

    if sorted(set(CyfrX)) == sorted(set(CyfrY)):
        return True
    else:
        return False



for punkt in Dane:
    if Czycyfropodobne(punkt[0], punkt[1]):
        ilosc += 1

print(ilosc)