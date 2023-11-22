F = open("slowa.txt")

Slowa = []

for line in F:
    Slowa.append(line.rstrip())

###################################################
### Podpunkt A)

ilosc = 0

for i in range(len(Slowa)):
    if Slowa[i].count('0') > Slowa[i].count('1'):
        ilosc += 1

print(ilosc)
print()

#######################################################
### Podpunkt B)

ilosc1 = 0
for i in range(len(Slowa)):
    czyPrawda = True
    for j in range(len(Slowa[i])-1):
        if int(Slowa[i][j]) > int(Slowa[i][j+1]) or Slowa[i].count('0') == 0 or Slowa[i].count('1') == 0 :
            czyPrawda = False
            break

    if czyPrawda:
        ilosc1 +=1

print(ilosc1)
print()
##################################################################
### Podpunkt C)

maksdlugoscW = 0

for i in range(len(Slowa)):
    dlugosc = 0
    maksdlugosc = 0

    for j in range(len(Slowa[i])):
        if Slowa[i][j] == '0':
            dlugosc += 1

            if dlugosc > maksdlugosc:
                maksdlugosc = dlugosc

        else:
            dlugosc = 0

    if maksdlugosc > maksdlugoscW:
        maksdlugoscW = maksdlugosc

    if maksdlugosc == 10:
        print(Slowa[i])

print()
print(maksdlugoscW)

