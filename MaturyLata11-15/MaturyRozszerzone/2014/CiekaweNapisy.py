Napisy = open("NAPIS.TXT").read().split()


###################################################
### Podpunkt A)

def czyPierwsza(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

ilosc = 0

for i in range(len(Napisy)):
    suma = 0
    for j in range(len(Napisy[i])):
        suma += ord(Napisy[i][j])

    if czyPierwsza(suma):
        ilosc += 1

print(ilosc)
print()

################################################
### Podpunkt B)

for i in range(len(Napisy)):
    czyPrawda = True
    for j in range(len(Napisy[i])-1):
        if ord(Napisy[i][j]) >= ord(Napisy[i][j+1]):
            czyPrawda = False
            break

    if czyPrawda:
        print(Napisy[i])
print()


######################################################
### Podpunkt C)

Opcje = []

for i in range(len(Napisy)):
    if Napisy[i] not in Opcje:
        Opcje.append(Napisy[i])

for i in range(len(Opcje)):
    if Napisy.count(Opcje[i]) > 1:
        print(Opcje[i])

