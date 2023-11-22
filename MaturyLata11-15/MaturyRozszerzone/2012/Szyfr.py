TJ = open("tj.txt").read().split()

Klucz1 = open("klucze1.txt").read().split()

print(TJ)
####################################################3
##Podpunkt A)
"""
for i in range(len(TJ)):
    wyraz = ''
    k = 0
    for j in range(len(TJ[i])):
        litera = ord(TJ[i][j]) + ord(Klucz1[i][k]) - 64

        if litera > 90:
            litera -= 26

        wyraz += chr(litera)

        k += 1

        if k == len(Klucz1[i]):
            k=0

    print(wyraz)
"""
##################################################
#### Podpunkt B)

SZ = open("sz.txt").read().split()
Klucze2 = open("klucze2.txt").read().split()


def deszyfruj(tj, k):
    litera = ord(tj) - ord(k) + 64

    if litera < 65:
        litera += 26

    return chr(litera)

for i in range(len(SZ)):
    slowo = ''
    k = 0
    for j in range(len(SZ[i])):
        slowo += deszyfruj(SZ[i][j], Klucze2[i][k])

        k += 1

        if k == len(Klucze2[i]):
            k = 0

    print(slowo)

