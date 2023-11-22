F = open("dane_systemy1.txt")
G = open("dane_systemy2.txt")
H = open("dane_systemy3.txt")

Czas1 = []
Czas2 = []
Czas3 = []

Temp1 = []
Temp2 = []
Temp3 = []

for line in F:
    x = line.split()
    Czas1.append(int(x[0], 2))
    Temp1.append(int(x[1], 2))

for line in G:
    x = line.split()
    Czas2.append(int(x[0], 4))
    Temp2.append(int(x[1], 4))

for line in H:
    x = line.split()
    Czas3.append(int(x[0], 8))
    Temp3.append(int(x[1], 8))

#####################################
## 58.1

print(bin(min(Temp1)).replace('0b', ''))
print(bin(min(Temp2)).replace('0b', ''))
print(bin(min(Temp3)).replace('0b', ''))
print('\n')

########################################
### 58.2

ilosc = 0
for i in range(len(Czas1)):

    if Czas1[i] != (12 + i * 24):

        if Czas2[i] != (12 + i * 24):

            if Czas3[i] != (12 + i * 24):
                ilosc += 1

print(ilosc)
print('\n')
##########################################
### 58.3
ilosc1 = 1
for i in range(1, len(Temp1)):
    if int(Temp1[i] > max(Temp1[:i])) or Temp2[i] > max(Temp2[:i]) or Temp3[i] > max(Temp3[:i]):
        ilosc1 += 1

print(ilosc1)
print("\n")

#########################################
### 58.4
from math import ceil, floor


maks = 0
for i in range(len(Temp1)):
    for j in range(i+1, int(len(Temp1))):
        skok = ceil((Temp1[i] - Temp1[j]) ** 2 / abs(i - j))
        if skok > maks:
            maks = skok

print(maks)






