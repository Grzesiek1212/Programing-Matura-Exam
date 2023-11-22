F = open("punkty.txt")

Dane = []

for line in F:
    Dane.append(line.split())

import math

def Odleglosc(x,y,m,n):
    return math.sqrt((x-m)**2+(y-n)**2)

punktmax = []
odlegoscmax = 0

for punktA in Dane:
    for punktB in Dane:
        x = Odleglosc(int(punktA[0]), int(punktA[1]), int(punktB[0]), int(punktB[1]))
        if x > odlegoscmax:
            odlegoscmax = x
            punktmax.clear()
            punktmax.append(punktA)
            punktmax.append(punktB)

print(punktmax)
print(round(odlegoscmax,0))

