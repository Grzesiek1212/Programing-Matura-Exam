F = open("liczby.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def CzyPotega3(x):
    while x > 1:
        x = x / 3

    if x == 1:
        return True
    else:
        return False

ilosc = 0

for liczba in Dane:
    if CzyPotega3(int(liczba)):
        ilosc += 1

print(ilosc)