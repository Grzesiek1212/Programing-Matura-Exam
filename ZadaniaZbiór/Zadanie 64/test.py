we = open("dane_obrazki.txt")
obrazki = []
bity = []
obrazek = []
bit = []
for line in we:
    if line != "\n" and len(line.strip()) != 20:
        obrazek.append(line.strip()[:-1])
        bit.append(line.strip()[-1])
    elif len(line.strip()) == 20:
        bit.append(line.strip())
    else:
        obrazki.append(obrazek)
        bity.append(bit)
        obrazek = []
        bit = []


print(len(obrazki))

