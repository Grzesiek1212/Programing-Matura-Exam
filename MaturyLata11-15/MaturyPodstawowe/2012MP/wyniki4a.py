F = open("cyfry.txt")
Lista = []

for line in F:
    Lista.append(line.rstrip())


print('----------------------- Zadanie 1 --------------------')
liczbaParz = 0
for i in range(len(Lista)):
    if int(Lista[i]) % 2 == 0:
        liczbaParz += 1

print(liczbaParz)




print('----------------------- Zadanie 2--------------------')


def sumaCyfr(x):
    suma = 0
    while x:
        suma += x % 10
        x = x//10
    return suma


"""maks = 0

for i in range(len(Lista)):
    if sumaCyfr(int(Lista[i])) > maks:
        maks = sumaCyfr(int(Lista[i]))
        
print(maks)

minn = int(Lista[1])

for i in range(len(Lista)):
    if sumaCyfr(int(Lista[i])) < minn:
        minn = sumaCyfr(int(Lista[i]))
        
print(minn)"""

Sumy = []

for i in range(len(Lista)):
    Sumy.append(sumaCyfr(int(Lista[i])))

print(Lista[Sumy.index(max(Sumy))])
print(Lista[Sumy.index(min(Sumy))])





print('----------------------- Zadanie 3 --------------------')

"""def ciagRosnacy(x):
    cyfra = 10
    while x:
        if x % 10 < cyfra:
            cyfra = x % 10
            x = x//10
        else:
            return False
    return True

for i in range(len(Lista)):
    if ciagRosnacy(int(Lista[i])):
        print(Lista[i])"""

for i in range(len(Lista)):
    czyPrawda = True

    for j in range(len(Lista[i])-1):
        if int(Lista[i][j]) >= int(Lista[i][j+1]):
            czyPrawda = False

    if czyPrawda:
        print(Lista[i])
