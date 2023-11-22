F = open('dane_6_2.txt')
Dane = []

for line in F:
    Dane.append(line.split())

for i in range(len(Dane)):
    if len(Dane[i]) == 1:
        print(i)