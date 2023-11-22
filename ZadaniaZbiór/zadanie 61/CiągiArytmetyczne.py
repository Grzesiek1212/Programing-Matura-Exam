F = open("ciagi.txt")

Ciagi = []
Ciagi1 = []
IloscWyraz = []

for line in F:
    Ciagi.append(line.split())

for i in range(0, 200, 2):
    Ciagi1.append(Ciagi[i+1])
    IloscWyraz.append(Ciagi[i])

##################################################
#### 61.1
ilosc = 0
maksR = 0
for i in range(len(Ciagi1)):
    r = int(Ciagi1[i][1]) - int(Ciagi1[i][0])
    czyprawda = True
    for j in range(len(Ciagi1[i])-1):
        if int(Ciagi1[i][j]) + r != int(Ciagi1[i][j+1]):
           czyprawda = False
           break

    if czyprawda:
        ilosc += 1
        if r > maksR:
            maksR = r

print(ilosc)
print(maksR)
print("\n")
##################################################
### 61.2
from math import ceil

for i in range(len(Ciagi1)):
    szescian = []
    for j in range(len(Ciagi1[i])):
        if (float(ceil(int(Ciagi1[i][j]) ** (1/3)))) ** 3 == (int(Ciagi1[i][j])):
            szescian.append(int(Ciagi1[i][j]))

    if len(szescian)>0:
        print(max(szescian))\

print()
Szesciany = []

for i in range(1, 101):
    Szesciany.append(i ** 3)

for i in range(len(Ciagi1)):
    najwiekszy = 0
    for j in range(len(Ciagi1[i])):
        if int(Ciagi1[i][j]) in Szesciany:
            if int(Ciagi1[i][j]) > najwiekszy:
                najwiekszy = int(Ciagi1[i][j])

    if najwiekszy != 0:
        print(najwiekszy)


