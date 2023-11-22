
ObrazkiCale = open("dane_obrazki.txt").read().split()

Obrazki =  []
i = 0

while i < len(ObrazkiCale):
    j = i + 21
    Obrazki.append(ObrazkiCale[i:j])
    i += 21

Obrazkiprzyklad = open("obrazek przykład.txt").read().split()

##########################################################
##########################################################

iloscczarnychmaks = 0
ilosc = 0
for obrazek in Obrazki:
    ilosc0 = 0
    ilosc1 = 0
    for i in range(20):
        for j in range(20):
            if obrazek[i][j] == '0':
                ilosc0 += 1

            else:
                ilosc1 += 1
    if ilosc1 > ilosc0:
        ilosc += 1

    if ilosc1 > iloscczarnychmaks:
        iloscczarnychmaks = ilosc1

print(ilosc)
print(iloscczarnychmaks)
print("\n")
print("\n")

##############################################
### Zadanie 64.2

ilosc = 0

def cwiartka1(x):
    cwiartka = ''
    for i in range(10):
        for j in range(10):
            cwiartka += x[i][j]
    return cwiartka

def cwiartka2(x):
    cwiartka = ''
    for i in range(10):
        for j in range(10, 20):
            cwiartka += x[i][j]
    return cwiartka

def cwiartka3(x):
    cwiartka = ''
    for i in range(10, 20):
        for j in range(10):
            cwiartka += x[i][j]
    return cwiartka

def cwiartka4(x):
    cwiartka = ''
    for i in range(10, 20):
        for j in range(10, 20):
            cwiartka += x[i][j]
    return cwiartka

for i in range(len(Obrazki)):
    if cwiartka1(Obrazki[i]) == cwiartka2(Obrazki[i]) == cwiartka3(Obrazki[i]) == cwiartka4(Obrazki[i]):
        ilosc += 1
        if ilosc == 1:
            for j in range(20):
                print(Obrazki[i][j][:20])

print()
print(ilosc)
print("\n")
print("\n")

#######################################################

def bitParzystosciPoziomo (wiersz):
    ilosc1 = 0
    for i in range(20):
        if wiersz[i] == '1':
            ilosc1 += 1
    if ilosc1 % 2 == 0:
        return 0
    else:
        return 1

def bitParzystosciPionowo (Tablica , numerKulumny):
    ilosc1 = 0
    for i in range(0, len(Tablica)-1):
        if Tablica[i][numerKulumny] == '1':
            ilosc1 += 1
    if ilosc1 % 2 == 0:
        return 0
    else:
        return 1


iloscObrazkowPoprawnych = 0
iloscObrazkowNaprawialnych = 0
iloscObrazkowNienaprawialnych = 0

maxbledow = 0

for obrazek in Obrazki:

    iloscNieprawedziwychPoziom = 0
    for i in range(len(obrazek)-1):
        ostatniWyraz = obrazek[i][-1]
        if int(ostatniWyraz) != bitParzystosciPoziomo(obrazek[i]):
            iloscNieprawedziwychPoziom += 1



    iloscNieprawedziwychPion = 0
    for j in range(len(obrazek)- 1):
        ostatniWyrazpion = obrazek[-1][j]
        if int(ostatniWyrazpion) != bitParzystosciPionowo(obrazek, j):
            iloscNieprawedziwychPion += 1

    if iloscNieprawedziwychPion + iloscNieprawedziwychPoziom > maxbledow:
        maxbledow = iloscNieprawedziwychPion + iloscNieprawedziwychPoziom

    if iloscNieprawedziwychPion + iloscNieprawedziwychPoziom == 0:
        iloscObrazkowPoprawnych += 1

    if iloscNieprawedziwychPion <= 1 and iloscNieprawedziwychPoziom <= 1 and (iloscNieprawedziwychPion == 1 or iloscNieprawedziwychPoziom == 1):
        iloscObrazkowNaprawialnych += 1

    if iloscNieprawedziwychPion > 1 or iloscNieprawedziwychPoziom > 1:
        iloscObrazkowNienaprawialnych += 1



print(iloscObrazkowPoprawnych)
print(iloscObrazkowNaprawialnych)
print(iloscObrazkowNienaprawialnych)
print(maxbledow)

print("\n")
print("\n")

##############################################################
### zadanie 64.4





z = 0
for obrazek in Obrazki:
    indekswiersza = 0
    indekskolumny = 0

    iloscNieprawedziwychPoziom = 0
    for i in range(len(obrazek)-1):
        ostatniWyraz = obrazek[i][-1]
        if int(ostatniWyraz) != bitParzystosciPoziomo(obrazek[i]):
            iloscNieprawedziwychPoziom += 1
            indekswiersza = i

    iloscNieprawedziwychPion = 0
    for j in range(len(obrazek) - 1):
        ostatniWyrazpion = obrazek[-1][j]
        if int(ostatniWyrazpion) != bitParzystosciPionowo(obrazek, j):
            iloscNieprawedziwychPion += 1
            indekskolumny = j

    if iloscNieprawedziwychPion == 1 and iloscNieprawedziwychPoziom == 1:
        print(f" obrazek numer { z + 1 },   numer wiersza: {indekswiersza + 1 },   numer kolumny: {indekskolumny + 1 }")

    if iloscNieprawedziwychPion == 0 and iloscNieprawedziwychPoziom == 1:
        print(f" obrazek numer {z + 1},   numer wiersza: {indekswiersza + 1},   numer kolumny: 21")

    if iloscNieprawedziwychPion == 1 and iloscNieprawedziwychPoziom == 0:
        print(f" obrazek numer {z + 1},   numer wiersza: 21,   numer kolumny: {indekskolumny + 1 }")


    z += 1









