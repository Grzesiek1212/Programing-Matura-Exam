F = open("pary.txt")

Dane = []
Dane_3 =[]
for line in F:
    Dane.append(line.split())

for i in range(len(Dane)):
    if int(Dane[i][0]) == len(Dane[i][1]):
        Dane_3.append(Dane[i])

najmnijsza = 0

def CzyMniejsza (x,y,z,m):
    if -x < z:
        return True
    if -x == z:
        if len(list(sorted(y))) < len(list(sorted(m))):
            return True

    return False

for i in range(len(Dane_3)):
    if CzyMniejsza(int(Dane_3[i][0]),Dane_3[i][1],int(Dane_3[najmnijsza][0]),Dane_3[najmnijsza][1]):
        najmnijsza = i

print(Dane_3[najmnijsza])


