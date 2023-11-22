F = open("napisy.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

slowo = ''
for i in range(19,len(Dane),20):
    slowo += Dane[i][(i+1)//20 - 1]

print(slowo)