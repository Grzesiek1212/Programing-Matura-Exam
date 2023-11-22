F = open("identyfikator.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

Numeratory = []

def Sumacyfr(x):
    suma = 0
    while int(x)>0:
        suma += int(x) % 10
        x = int(x) // 10
    return suma


for numerator in Dane:
    Numeratory.append(Sumacyfr(numerator[3:]))


maks = 0

for liczba in Numeratory:
    if liczba>maks:
        maks = liczba

for i in range(len(Numeratory)):
    if Numeratory[i] == maks:
        print(Dane[i])


