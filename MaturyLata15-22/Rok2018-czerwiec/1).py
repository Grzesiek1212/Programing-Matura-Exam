F = open("dane1.txt")
G = open("dane2.txt")

Dane1 = []
Dane2 = []

for line in F:
    Dane1.append(line.split())

for lol in G:
    Dane2.append(lol.split())

ilosc = 0

for i in range(len(Dane1)):
    if Dane1[i][-1] == Dane2[i][-1]:
        ilosc += 1

print(ilosc)