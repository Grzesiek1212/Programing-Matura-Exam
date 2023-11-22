F = open("hasla.txt")
Lista = []

for line in F:
    Lista.append(line.rstrip())

iloscParz = 0
iloscNieparz = 0

for i in range(len(Lista)):
    if len(Lista[i])%2 == 0 :
        iloscParz+=1
    else:
        iloscNieparz+=1

print(iloscParz)
print(iloscNieparz)
