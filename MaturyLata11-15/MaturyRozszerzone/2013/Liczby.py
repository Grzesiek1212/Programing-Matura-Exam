F = open("dane.txt")
Liczby = []

for line in F:
    Liczby.append(line.strip())

#######################################################
### Podpunkt A
ilosc = 0

for i in range(len(Liczby)):
    if Liczby[i][0] == Liczby[i][-1]:
        ilosc += 1

print(ilosc)

#######################################################
### Podpunkt B
ilosc1 = 0
Liczby10 = []

for i in range(len(Liczby)):
    x = int(Liczby[i], 8)
    Liczby10.append(str(x))

for i in range(len(Liczby10)):
    if Liczby10[i][0] == Liczby10[i][-1]:
        ilosc1 += 1

print(ilosc1)

####################################################
### Podpunkt C
print('\n')
Odpowiedzi = []

for i in range(len(Liczby)):
    czyPrawda = True
    for j in range(len(Liczby[i])-1):
        if Liczby[i][j] > Liczby[i][j+1]:
            czyPrawda = False
            break

    if czyPrawda:
        Odpowiedzi.append(int(Liczby[i]))



print(len(Odpowiedzi))
print()

print(max(Odpowiedzi))
print(min(Odpowiedzi))

print()
print()

def pod_c():
    wyniki = []
    dziesietne1 = Liczby
    for z in range(len(dziesietne1)):
        dziesietne1[z] = int(dziesietne1[z], 8)
    for i in range(len(Liczby)):
        pom = True
        for j in range(len(str(Liczby[i]))-1):
            if dziesietne1[i][j] > dziesietne1[i][j+1]:
                pom = False
                break
        if pom:
            wyniki.append(dziesietne1[i])

    print(max(wyniki), min(wyniki))
    print(dziesietne1)

pod_c()


