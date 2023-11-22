F = open("napisy.txt")
Lista = []

for line in F:
    Lista.append(line.rstrip())


print('----------------------- Podpunkt a) --------------------')


liczbaParzystych = 0

for i in range(len(Lista)):
    if len(Lista[i]) % 2 == 0:
        liczbaParzystych+=1

print(liczbaParzystych)

print('----------------------- Podpunkt b) --------------------')

"""def CzyLiczbaDana(x):
    iloscZero = 0
    iloscJeden = 0
    
    for i in range(len(x)):
        if int(x[i]) == 0:
            iloscZero+=1
            
        else:
            iloscJeden+=1
            
    if iloscZero == iloscJeden:
        return True
    
    else:
        return False

iloscPrawdziwych = 0
for i in range(len(Lista)):
    if CzyLiczbaDana((Lista[i])) == True :
        iloscPrawdziwych+=1

print(iloscPrawdziwych)"""

zera = 0
jedynki = 0

for i in range(len(Lista)):
    if Lista[i].count('0') == Lista[i].count('1'):
        zera+=1


print(zera)


print('----------------------- Podpunkt c) --------------------')

"""def sameZera(x):
    for i in range(len(x)):
        if x[i] == '1':
            return False
    return True
def sameJedynki(x):
    for i in range(len(x)):
        if x[i] == '0':
            return False
    return True

iloscSame1 = 0
iloscSame0 = 0

for i in range(len(Lista)):
    if sameZera(Lista[i]) == True:
        iloscSame0 += 1
    elif sameJedynki(Lista[i]) == True:
        iloscSame1 += 1

print(iloscSame0)
print(iloscSame1)"""

zera = 0
jedynki = 0

for i in range(len(Lista)):
    if Lista[i].count('0') == len(Lista[i]):
        zera += 1

    elif Lista[i].count('1') == len(Lista[i]):
        jedynki += 1

print(zera)
print(jedynki)

print('----------------------- Podpunkt d) --------------------')

for k in range(2,17):
    ilosck= 0
    for i in range(len(Lista)):
        if len(Lista[i]) == k:
            ilosck+=1
    print(f"ilość liczb o liczbie cyfr {k} jest równe {ilosck}")




