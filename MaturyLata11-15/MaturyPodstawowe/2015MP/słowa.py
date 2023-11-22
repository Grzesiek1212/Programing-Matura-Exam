F = open("slowa.txt")
G = open("nowe.txt")

Slowa = []
Nowe = []

for line in F:
    Slowa.append(line.rstrip())

for line in G:
    Nowe.append(line.rstrip())

#####################################################
## 5.1

for n in range(1,13):
    iloscA = 0
    for i in range(len(Slowa)):
        if len(Slowa[i]) == n:
            iloscA += 1

    print(F" wierszy z {n} literowymi słowami jest {iloscA} ")

print()
print()
##########################################################
## 5.2


for i in range(len(Nowe)):
    ilosc1 = 0
    ilosc2 = 0
    for j in range(len(Slowa)):
        if Slowa[j] == Nowe[i]:
            ilosc1 += 1
        elif Slowa[j] == Nowe[i][::-1]:
            ilosc2 += 1


    print(f"słowo {Nowe[i]} występuje {ilosc1} w pliku Słowa a odbić lustrzanych tego słowa jest {ilosc2}.")


for i in range(len(Nowe)):
    print(Nowe[i], Slowa.count(Nowe[i]), Slowa.count(Nowe[i][::-1]))