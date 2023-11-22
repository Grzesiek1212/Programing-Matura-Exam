F = open("liczby1.txt")
G = open("liczby2.txt")

Liczby1 = []
Liczby2 = []

for line in F:
    Liczby1.append(int(line.rstrip(), 8))

for line in G:
    Liczby2.append(int(line.rstrip()))

#############################################################
### 62.1
print("-------------------podponkt 1 ---------------------")
print(oct(max(Liczby1)).replace('0o', ''))
print(oct(min(Liczby1)).replace('0o', ''))
##############################################################
### 62.2
print("-------------------podponkt 2 ---------------------")
maksdlugosc = 0
wyrazstart = 0
dlugosc = 1
for i in range(len(Liczby2)-1):
    if Liczby2[i] <= Liczby2[i+1]:
        dlugosc += 1
        if dlugosc > maksdlugosc:
            maksdlugosc = dlugosc
            wyrazstart = Liczby2[i - maksdlugosc + 2]
    else:
        dlugosc = 1

print(maksdlugosc)
print(wyrazstart)
########################################################
#### 62.3
iloscrownych = 0
iloscwiekszych = 0

for i in range(len(Liczby1)):
    if Liczby1[i] == Liczby2[i]:
        iloscrownych+=1

    if Liczby1[i] > Liczby2[i]:
        iloscwiekszych += 1
print("-------------------podponkt 3 ---------------------")
print(iloscrownych)
print(iloscwiekszych)

#########################################################
#### 62.4
print("-------------------podponkt 4 ---------------------")
ilosc1 = 0
ilosc2 = 0

for i in Liczby2:
    x = str(i)
    y = oct(i)
    ilosc1 += x.count('6')
    ilosc2 += y.count('6')


print(ilosc1)
print(ilosc2)

print()



ile = lambda x : str(x).count('6')


print(sum(list(map(ile, Liczby2))), sum(list(map(ile, [oct(i) for i in Liczby2]))))