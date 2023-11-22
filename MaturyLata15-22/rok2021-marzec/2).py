F = open("galerie.txt")

Dane = []

for line in F:
    Dane.append(line.split())



for galeria in Dane:
    sklepy = []
    for i in range(2, len(galeria), 2):
        sklepy.append(int(galeria[i])*int(galeria[i+1]))

    ilosc = 0

    for j in range(len(sklepy)):
        if sklepy[j] != 0:
            ilosc += 1

    print(galeria[1], sum(sklepy), ilosc)
