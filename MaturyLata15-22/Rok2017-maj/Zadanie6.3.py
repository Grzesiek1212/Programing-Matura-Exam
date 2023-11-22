F = open("dane.txt")
Dane = []

for line in F:
    Dane.append(line.split())

def Kontrastujacy(i, j , Tablica):
    ilosc = 0
    if i - 1 >= 0:
        if abs(int(Tablica[i-1][j]) - int(Tablica[i][j])) > 128:
            ilosc += 1

    if i + 1 <= 199:
        if abs(int(Tablica[i+1][j]) - int(Tablica[i][j])) > 128:
            ilosc += 1

    if j + 1 <= 319:
        if abs(int(Tablica[i][j+1]) - int(Tablica[i][j])) > 128:
            ilosc += 1

    if j - 1 >= 0:
        if abs(int(Tablica[i][j-1]) - int(Tablica[i][j])) > 128:
            ilosc += 1

    if ilosc >= 1:
        return True
    else:
        return False

ilosc = 0

for i in range(len(Dane)):
    for j in range(len(Dane[i])):
        if Kontrastujacy(i, j, Dane):
            ilosc += 1


print(ilosc)

