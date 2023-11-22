F = open("pary.txt")

Dane = []
Dane_1 =[]
for line in F:
    Dane.append(line.split())

for i in range(len(Dane)):
    Dane_1.append(int(Dane[i][0]))

def CzyPierwsza(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for i in range(len(Dane_1)):
    liczba = Dane_1[i]
    if liczba % 2 == 0 :
        for j in range(2, Dane_1[i]):
            if CzyPierwsza(j):
                if CzyPierwsza(Dane_1[i]-j):
                    print(liczba, j, Dane_1[i]-j)
                    break


