F = open("wykreslanka.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

for i in range(len(Dane)):
    for j in range(len(Dane[i])- 5):
        if Dane[i][j:j+6] == "matura":
            print(i)
            break

print()
for j in range(len(Dane[0])):
    slowo = ''
    for i in range(len(Dane)):
        slowo += Dane[i][j]

    if 'matura' in slowo:
        print(j)
