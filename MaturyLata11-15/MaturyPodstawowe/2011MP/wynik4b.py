F = open("hasla.txt")
Lista = []

for line in F:
    Lista.append(line.rstrip())

for i in range(len(Lista)):
    if Lista[i] == Lista[i][::-1]:
        print(Lista[i])

print()