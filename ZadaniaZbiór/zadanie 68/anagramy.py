F = open("dane_napisy.txt")

Napisy = []
Napisy1 = []

for line in F:
    Napisy.append(line.split())

for k in Napisy:
    x = k[0]
    y = k[1]
    Napisy1.append(x)
    Napisy1.append(y)

#######################################################
### 68.1
ilosc = 0

for i in range(len(Napisy)):
    a = Napisy[i][0]
    b = Napisy[i][1]
    if len(a) == len(b):
        czyPrawda = True
        for j in range(len(a)-1):
            if a[j] != a[j+1] or b[j] != b[j+1]:
                czyPrawda = False
                break

        if czyPrawda:
            ilosc += 1

print(ilosc)
print("\n")

#########################################################
### 68.2
ilosc1 = 0

for i in range(len(Napisy)):
    a = Napisy[i][0]
    b = Napisy[i][1]
    if len(a) == len(b) and sorted(a) == sorted(b):
        ilosc1 += 1

print(ilosc1)
print("\n")
#######################################################
### 68.3

maks = 0

for i in range(len(Napisy1)):
    k = 0
    for j in range(len(Napisy1)):
        if sorted(Napisy1[i]) == sorted(Napisy1[j]):
            k += 1
            if k > maks:
                maks = k

print(maks)
