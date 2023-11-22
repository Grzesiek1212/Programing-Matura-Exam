F = open("dane.txt")
Ds = open("dane.txt").read().rstrip()
Lista = []
print(F)
for line in F:
    Lista.append(line.rstrip())

for i in range(len(Lista)):
    if Lista[i] == Lista[i][::-1]:
        print(Lista[i])