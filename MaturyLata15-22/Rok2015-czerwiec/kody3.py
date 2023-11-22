F = open('kody.txt')
G = open('cyfra_kodkreskowy.txt')
W = open('kody3.txt', 'w')

Kody = []
Cyfra = []

for line in F:
    Kody.append(line.rstrip())

for x in G:
    Cyfra.append(x.split())

for i in range(len(Kody)):
    liczba1 = 0
    liczba2 = 0
    liczba = 0
    liczbakreskowy = '11011010'
    for j in range(len(Kody[i])):
        if j % 2 == 0:
            liczba2 += int(Kody[i][j])
        else:
            liczba1 += int(Kody[i][j])

        for l in Cyfra:
            if l[0] == Kody[i][j]:
                liczbakreskowy += l[1]

    liczba += 3 * liczba1 + liczba2
    liczba = (10 - (liczba % 10)) % 10

    for x in Cyfra:
        if int(x[0]) == liczba:
            liczbakreskowy += x[1]
    liczbakreskowy += '11010110'
    W.write(f'{liczbakreskowy}\n')




F.close()
G.close()
W.close()
