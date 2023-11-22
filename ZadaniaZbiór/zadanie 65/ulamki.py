F = open("dane_ulamki.txt")

Ulamki = []

for line in F:
    Ulamki.append(line.split())

##################################################
### 65.1

licznik = 0
mianownik = 0
wartosc = int(Ulamki[0][0]) / int(Ulamki[0][1])

for i in range(len(Ulamki)):
    if int(Ulamki[i][0]) / int(Ulamki[i][1]) < wartosc:
        wartosc = int(Ulamki[i][0]) / int(Ulamki[i][1])
        licznik = Ulamki[i][0]
        mianownik = Ulamki[i][1]

print(licznik)
print(mianownik)
print("\n")

####################################################
### 65.2

def czyNieJestskracalny(x, y):
    for i in range(2, max(x,y) + 1):
        if x % i == 0 and y % i == 0 or x == y:
            return False

    return True


ilosc = 0

for i in range(len(Ulamki)):
    licznik1 = int(Ulamki[i][0])
    mianownik1 = int(Ulamki[i][1])

    if czyNieJestskracalny(licznik1, mianownik1):
        ilosc += 1


print(ilosc)
print("\n")

######################################################
### 65.3

def skracanie(x, y):
    if x == y:
        x = int(x / y)
    for j in range(20):
        for i in range(2, max(x,y) + 1):
            if x % i == 0 and y % i == 0 or x == y:
                x = int(x / i)
                y = int(y / i)

    return x

def s2kracanie(a,b):
    return a // nwd(a,b) ### lepszy sposób

suma = 0

for i in range(len(Ulamki)):
    m = int(Ulamki[i][0])
    n = int(Ulamki[i][1])
    suma += skracanie(m, n)

print(suma)
print("\n")
###################################################
### 65.4

szukana = 0

for i in range(len(Ulamki)):
    mnoznik = 0
    p = int(Ulamki[i][0])
    k = int(Ulamki[i][1])
    mnoznik = int(573300 / k)
    szukana += (p * mnoznik)

print(szukana)
