F = open("sygnaly.txt")

Sygnaly = []

for line in F:
    Sygnaly.append(line.rstrip())

kod = ''
for i in range(39,len(Sygnaly),40):
    kod += Sygnaly[i][9]

print(kod)