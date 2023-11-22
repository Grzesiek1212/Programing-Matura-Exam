F = open("liczby.txt")
Liczby = []

for line in F:
    Liczby.append(line.rstrip())

Liczby10 = []

for i in range(len(Liczby)):
    liczba10 = 0
    for j in range(len(Liczby[i])):
        liczba10 += int(Liczby[i][len(Liczby[i])-j-1]) * 2**j
    Liczby10.append(liczba10)


print(min(Liczby10), Liczby10.index(min(Liczby10))+1)
print(max(Liczby10), Liczby10.index(max(Liczby10))+1)
