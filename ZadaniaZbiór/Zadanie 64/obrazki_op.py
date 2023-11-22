with open("dane_obrazki.txt") as dane:
    plik = dane.read().splitlines()

def wypisz_obrazek(obrazek):
    for i in range(21):
        print(obrazek[i])
    print(("\n---------------------\n"))


# def sprawdzanie_kolumn(plansza):
#     flaga = True
#     for i in range(20):
#         ilosc = 0
#         for j in range(20):
#             ilosc += int(plansza[j][i])
#         print(plansza[i])
#         if ilosc % 2 != int(plansza[i][20]):
#             flaga = False
#     return flaga
def sprawdzanie_kolumn(plansza):
    flaga = True
    for i in range(20):
        ilosc = 0
        for j in range(20):
            ilosc += int(plansza[j][i])
        if ilosc % 2 != int(plansza[20][i]):
            flaga = False
    return flaga




obrazki = []
for numer_obrazka in range(200):
    obrazek = []
    for wiersz in range(21):
        obrazek.append(plik[22 * numer_obrazka + wiersz])
    obrazki.append(obrazek)



def a():
    for numer_obrazka in range(200):
        wypisz_obrazek(obrazki[numer_obrazka])
    rewersy = 0
    jed_maks = 0
    for numer_obrazka in range(200):
        jedynki = 0
        for wiersz in range(20):
            jedynki += obrazki[numer_obrazka][wiersz][:20].count("1")

        if jedynki > 200:
            rewersy += 1
        if jedynki > jed_maks:
            jed_maks = jedynki
    print(jed_maks)
    print(rewersy)

a()

def b():
    licznik = 0
    for numer_obrazka in range(200):
        takie_same = True
        for wiersz in range(10):
            if obrazki[numer_obrazka][wiersz][0:10] != obrazki[numer_obrazka][wiersz][10:20]:
                takie_same = False
            if obrazki[numer_obrazka][wiersz][0:10] != obrazki[numer_obrazka][wiersz+10][0:10]:
                takie_same = False
            if obrazki[numer_obrazka][wiersz][0:10] != obrazki[numer_obrazka][wiersz+10][10:20]:
                takie_same = False
        if takie_same:
            licznik += 1
    print(licznik)
b()

def c():
    suma_poprawnych = 0
    for i in range(200):
        flaga = True
        if not sprawdzanie_kolumn(obrazki[i]):
            flaga = False
        for wiersz in range(20):
            if (obrazki[i][wiersz][:20]).count("1") % 2 != int(obrazki[i][wiersz][20]):
                flaga = False
        if flaga:
            suma_poprawnych += 1
    print(suma_poprawnych)

c()