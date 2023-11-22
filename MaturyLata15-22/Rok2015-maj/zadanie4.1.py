F = open("liczby.txt")
Liczby = []

for line in F:
    Liczby.append(line.rstrip())

wynik = 0

for x in Liczby:
    if x.count('0') > x.count('1'):
        wynik += 1

W = open('wynik4.txt', 'w')


W.write('Podpunkt 1 \n')
W.write(f'{wynik}')


F.close()
W.close()



