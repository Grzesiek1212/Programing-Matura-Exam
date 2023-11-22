F = open("punkty.txt")

Dane = []

for line in F:
    Dane.append(line.split())

def czyNalezy(x,y):
    if abs(int(x)) < 5000 and abs(int(y)) < 5000:
        return True
    else:
        return False

def czyW(x,y):
    if (abs(int(x)) == 5000 and abs(int(y)) <= 5000) or (abs(int(x)) <= 5000 and abs(int(y)) == 5000) :
        return True
    else:
        return False

iloscNA = 0
iloscPOZA = 0
iloscW = 0

for punkt in Dane:
    if czyNalezy(punkt[0], punkt[1]):
        iloscW += 1

    elif czyW(punkt[0], punkt[1]):
        iloscNA += 1

    else:
        iloscPOZA += 1

print(iloscW)
print(iloscNA)
print(iloscPOZA)



