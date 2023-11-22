F = open("binarne.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def TwoToDec(x):
    liczba10 = 0
    for i in range(len(x)):
        liczba10 += int(x[i]) * 2**(len(x)-i-1)

    return liczba10

napis = ''
liczbamaks = 0

for liczba in Dane:
    if TwoToDec(liczba) > liczbamaks and TwoToDec(liczba) <= 65535:
        liczbamaks = TwoToDec(liczba)
        napis = liczba

print(napis, liczbamaks)