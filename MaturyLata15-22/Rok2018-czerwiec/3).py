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
    if sorted(set(Dane1[i])) == sorted(set(Dane2[i])):
        ilosc += 1
        print(i+1)

print()
print(ilosc)