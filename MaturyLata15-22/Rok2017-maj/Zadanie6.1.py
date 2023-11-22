F = open("dane.txt")
Dane = []

for line in F:
    Dane.append(line.split())

pikselmin = int(Dane[0][0]) # najciemniejszy
pikselmax = 0   ## najjasniejszy

for wiersz in Dane:
    for i in range(len(wiersz)):
        if int(wiersz[i]) > pikselmax:
            pikselmax = int(wiersz[i])

        if int(wiersz[i]) < pikselmin:
            pikselmin = int(wiersz[i])

print(pikselmin)
print(pikselmax)