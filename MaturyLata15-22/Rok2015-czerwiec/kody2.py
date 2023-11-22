F = open('kody.txt')
G = open('cyfra_kodkreskowy.txt')
W = open('kody2.txt', 'w')

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
    for j in range(len(Kody[i])):
        if j % 2 == 0:
            liczba2 += int(Kody[i][j])
        else:
            liczba1 += int(Kody[i][j])

    liczba += 3 * liczba1 + liczba2
    liczba = (10 - (liczba % 10)) % 10
    for l in Cyfra:
        if int(l[0]) == liczba:
            W.write(f'{int(l[0]), int(l[1])}\n')


F.close()
G.close()
W.close()




