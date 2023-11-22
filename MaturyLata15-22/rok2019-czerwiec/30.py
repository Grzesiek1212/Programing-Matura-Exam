F = open("pierwsze.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def W(n):
    sumacyfr = 0
    while n > 0:
        sumacyfr += n % 10
        n = n//10
    return sumacyfr

def waga(n):
    while len(n) > 1:
        n = str(W(int(n)))
    return n

ilosc = 0
for liczba in Dane:
    if waga(liczba) == '1':
        ilosc += 1

print(ilosc)
