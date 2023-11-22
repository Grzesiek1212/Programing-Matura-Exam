F = open("napisy.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

Alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Q', 'T', 'U', 'V','W', 'X', 'Y', 'Z']


haslo = ''
for wyraz in Dane:
    Liczby = []
    for i in range(len(wyraz)):
        if wyraz[i] not in Alfabet:
            Liczby.append(wyraz[i])

    if len(Liczby) % 2 == 1:
        Liczby.pop(-1)

    LiczbyG = []
    for j in range(0,len(Liczby),2):
        LiczbyG.append(int(Liczby[j]+Liczby[j+1]))

    for z in range(len(LiczbyG)):
        if LiczbyG[z] > 64 and LiczbyG[z] < 91:
            haslo += chr(LiczbyG[z])




for i in range(len(haslo)-4):
    if haslo[i:i+3] == 'XXX':
        haslo = haslo[:i+3]
        break


print(haslo)