F = open("sygnaly.txt")

Sygnaly = []

for line in F:
    Sygnaly.append(line.rstrip())

for slowo in Sygnaly:
    czyprawda = True
    for i in range(len(slowo)):
        for j in range(len(slowo)):
            if abs(ord(slowo[i]) - ord(slowo[j])) > 10:
                czyprawda = False
                break
    if czyprawda:
        print(slowo)


