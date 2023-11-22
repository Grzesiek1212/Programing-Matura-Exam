F = open("punkty.txt")

Dane = []

for line in F:
    Dane.append(line.split())

def Czypierwsza(x):
    if x < 2:
        return False
    for i in range(2,x//2):
        if x % i == 0:
            return False

    return True

ilosc = 0

for punkt in Dane:
    if Czypierwsza(int(punkt[0])) and Czypierwsza(int(punkt[1])):
        ilosc += 1

print(ilosc)