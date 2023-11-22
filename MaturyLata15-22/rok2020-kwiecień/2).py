F = open("dane4.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

pierwszy = ''
ostatni = ''
najdluzszy = 0
indeks = 0


for i in range(len(Dane)-2):
    luka = abs(int(Dane[i]) - int(Dane[i+1]))
    j = i + 1
    dlugosc = 2
    while luka == abs(int(Dane[j]) - int(Dane[j+1])) :
        dlugosc += 1
        if dlugosc > najdluzszy:
            ostatni = Dane[j+1]
            najdluzszy = dlugosc
            indeks = j+1
        j += 1

pierwszy = Dane[indeks-16]
print(najdluzszy, ostatni, pierwszy)
