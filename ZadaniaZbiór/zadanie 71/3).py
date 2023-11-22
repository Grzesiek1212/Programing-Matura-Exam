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

miejscazerowe = []

for i in range(500000):
    x = D(i/100000)
    if abs(x) < 0.000131:
        miejscazerowe.append(i/100000)

###### zrób jeszcze bisekcją

print(miejscazerowe)


