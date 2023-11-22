F = open('kody.txt')
W = open('kody1.txt', 'w')
Kody = []

for line in F:
    Kody.append(line.rstrip())

for i in range(len(Kody)):
    liczba1 = 0
    liczba2 = 0
    for j in range(len(Kody[i])):
        if j % 2 == 0:
            liczba2 += int(Kody[i][j])
        else:
            liczba1 += int(Kody[i][j])

    W.write(f'{int(Kody[i]), liczba1, liczba2}\n')

F.close()
W.close()