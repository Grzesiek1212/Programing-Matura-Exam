F = open("liczby.txt")
Liczby = []

for line in F:
    Liczby.append(line.rstrip())

####################################################
### Podpunkt A)

ilosc = 0

for i in range(len(Liczby)):
    if int(Liczby[i], 2) % 2 == 0:
        ilosc += 1

print(ilosc)


print()
print()
########################################################
### Podpunkt B)

maksDZ = 0
maksDW = 0

for i in range(len(Liczby)):
    if int(Liczby[i], 2) > maksDZ:
        maksDZ = int(Liczby[i], 2)
        maksDW = Liczby[i]

print(maksDZ)
print(maksDW)

print()
print()
#############################################
### Podpunkt C)

iloscL = 0
suma = 0

for i in range(len(Liczby)):
    if len(Liczby[i]) == 9:
        iloscL += 1
        suma += int(Liczby[i], 2)

print(iloscL)
print(bin(suma).replace('0b', ''))

