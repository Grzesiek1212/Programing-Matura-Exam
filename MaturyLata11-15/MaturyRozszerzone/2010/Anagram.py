############################################
#wczytanie danych
F = open("anagram.txt")

Anagramy = []

for line in F:
    Anagramy.append(line.split())


########################################################33
#podpunkt A

for i in range(len(Anagramy)):
    ilosc = len(Anagramy[i][0])
    czyPrawda = True

    for j in range(len(Anagramy[i])):
        if len(Anagramy[i][j]) != ilosc:
            czyPrawda = False

    if czyPrawda:
        print(Anagramy[i])


print()
print()
###################################################################
### podpunkt B

def anagram(x, y):
    if sorted(x) == sorted(y):
        return True

for i in range(len(Anagramy)):
    ilosck = 0
    for j in range(len(Anagramy[i])):
        if anagram(Anagramy[i][0], Anagramy[i][j]):
            ilosck += 1

    if ilosck == 5:
        print(Anagramy[i])





