F = open("liczby.txt")

Liczby = []

for line in F:
    x = line.rstrip()
    Liczby.append(int(x))

#########################################
### 60.1

Odpowiedzi = []

for i in range(len(Liczby)):
    if Liczby[i] < 1000:
        Odpowiedzi.append(Liczby[i])

print(len(Odpowiedzi))
print(Odpowiedzi[-2], Odpowiedzi[-1])
print("\n")
##########################################
#### 60.2

for i in range(len(Liczby)):
    Dzielniki = []
    for j in range(1, Liczby[i]//2 + 1):
        if Liczby[i] % j == 0:
            Dzielniki.append(j)
    Dzielniki.append(Liczby[i])

    if len(Dzielniki) == 18:
        print(Liczby[i])
        print(Dzielniki)
        print()

print()
##############################################################
#### 60.3

def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a

liczbypPierwsze = []

for j in range(len(Liczby)):
    czypolPierwsza = True
    for i in range(len(Liczby)):
        if nwd(Liczby[j], Liczby[i]) != 1 and j != i:
            czypolPierwsza = False

    if czypolPierwsza:
        liczbypPierwsze.append(Liczby[j])
print(max(liczbypPierwsze))





