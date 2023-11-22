F = open("liczby.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def spelnia(x):
    suma = 0
    while x > 0:
        cyfra = x % 10
        iloczyn = 1
        if cyfra == 0 :
            suma += 1
        else:
            for i in range(1,cyfra+1):
                iloczyn *= i
            suma += iloczyn
        x = x //10

    return suma

for liczba in Dane:
    if int(liczba) == spelnia(int(liczba)):
        print(liczba)