F = open("hasla.txt")
Lista = []

for line in F:
    Lista.append(line.rstrip())


print()
for i in range(len(Lista)):
    for j in range(len(Lista[i])-1):
        if ord(Lista[i][j]) + ord(Lista[i][j+1]) == 220:
            print(Lista[i])
            break