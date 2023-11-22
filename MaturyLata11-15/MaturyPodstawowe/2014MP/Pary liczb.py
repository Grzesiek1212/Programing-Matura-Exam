F = open("PARY_LICZB.TXT")

Pary = []

for line in F:
    x = line.split()
    Pary.append([int(x[0]), int(x[1])])

###################################################
### Podpunkt A)


ilosc = 0
for i in range(len(Pary)):
    if Pary[i][0] % Pary[i][1] == 0 or Pary[i][1] % Pary[i][0] == 0:
            ilosc+=1

print(ilosc)

##################################################
## Podpunkt B)

def nwd(x, y):
    while y:
        x, y = y, x%y
    return x

iloscB = 0

for i in range(len(Pary)):
    if nwd(Pary[i][0], Pary[i][1]) == 1:
        iloscB += 1

print(iloscB)

##########################################################
### Podpunkt C)

def sumaCyfr(x):
    suma = 0
    while x:
        suma += x % 10
        x = x // 10
    return suma

iloscC = 0

for i in range(len(Pary)):
    if sumaCyfr(Pary[i][0]) == sumaCyfr(Pary[i][1]):
        iloscC += 1

print(iloscC)

###################################################

