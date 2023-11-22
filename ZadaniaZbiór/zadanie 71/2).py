F = open("funkcja.txt")

Dane = []
Dane1 = []
for line in F:
    Dane.append(line.split())

def D(x):
    f = 0
    if x >= 0 and x < 1:
        for i in range(4):
            f += float(Dane[0][i]) * x**i

    if x >= 1 and x < 2:
        for i in range(4):
            f += float(Dane[1][i]) * x**i

    if x >= 2 and x < 3:
        for i in range(4):
            f += float(Dane[2][i]) * x ** i

    if x >= 3 and x < 4:
        for i in range(4):
            f += float(Dane[3][i]) * x ** i

    if x >= 4 and x < 5:
        for i in range(4):
            f += float(Dane[4][i]) * x ** i

    return round(f,5)

xmax = 0
ymax = 0

for i in range(5000):
    if D(i/1000) > ymax:
        xmax = i/1000
        ymax = D(xmax)

print(xmax, ymax)