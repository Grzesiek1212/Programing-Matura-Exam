F = open("liczby.txt")

Liczby = []

for line in F:
    x = line.rstrip()
    Liczby.append(int(x))

##############################################3
#### 59.1
'''''
def czyPierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

LiczbyPierwsze = []
for i in range(max(Liczby)//15 + 1):
    if czyPierwsza(i):
        LiczbyPierwsze.append(i)


ilosc = 0

for i in range(len(Liczby)):
    k = 0
    if not czyPierwsza(Liczby[i]):
        if Liczby[i] % 2 != 0:
            j = 0
            dzielniki = []
            while j < len(LiczbyPierwsze) and LiczbyPierwsze[j] <= 2 * Liczby[i]:
                if Liczby[i] % LiczbyPierwsze[j]:
                    if LiczbyPierwsze[j] in dzielniki:
                        k = 0
                        Liczby[i] = Liczby[i] // LiczbyPierwsze[j]
                        break
                    dzielniki.append(LiczbyPierwsze[j])
                    k += 1
                else:
                    j += 1

        if k == 3:
            ilosc += 1

print(ilosc)
'''

#################################################################################
### 59.2
def Czypalindrom(x):
    return x == int(str(x)[::-1])


ilosc = 0

for i in range(len(Liczby)):
    suma = Liczby[i] + int(str(Liczby[i])[::-1])
    if Czypalindrom(suma):
        ilosc += 1

print(ilosc)

#########################################################
###  59.3

Moc = []


def liczenieMocy(x):
    k = 0
    p = x

    while len(p) > 1:
        n = 1
        for j in range(len(p)):
            n *= int(p[j])
        p = str(n)
        k += 1

    return k

minn = Liczby[0]
maks = 0

for i in range(1,9):
    ilosc1 = 0
    for j in range(len(Liczby)):
        if liczenieMocy(str(Liczby[j])) == i:
            ilosc1 += 1
            if i == 1:
                if Liczby[j] > maks:
                    maks = Liczby[j]

                if Liczby[j] < minn:
                    minn = Liczby[j]

    print("Moc: ", i , "Ilosc: ", ilosc1)


print(maks)
print(minn)