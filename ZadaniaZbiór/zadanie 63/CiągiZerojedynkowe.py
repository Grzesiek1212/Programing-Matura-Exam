F = open("ciagi.txt")

Ciagi = []
Ciagi10 = []

for line in F:
    Ciagi.append(line.rstrip())

for i in Ciagi:
    Ciagi10.append(int(i, 2))

####################################################
### 63.1

for i in range(len(Ciagi)):
    if int(len(Ciagi[i])) % 2 == 0:
        polowa = len(Ciagi[i]) // 2
        if Ciagi[i][:polowa] == Ciagi[i][polowa:]:
            print(Ciagi[i])

print("\n")
###################################################
#### 63.2

ilosc = 0

for i in range(len(Ciagi)):
    flaga = 0
    czyprawda1 = True
    for j in range(len(Ciagi[i])):
        if flaga == 1 and int(Ciagi[i][j]) == 1:
            czyprawda1 = False
            break
        else:
            flaga = int(Ciagi[i][j])

    if czyprawda1:
        ilosc += 1

print(ilosc)
print("\n")

ilosc3 = 0

for i in range(len(Ciagi)):
    if '11' not in Ciagi[i]:
        ilosc3 += 1

print(ilosc3)

ile = lambda x: '11' not in x
print(len(list(filter(ile, Ciagi))))


print(sum([1 for i in Ciagi if '11' not in i]))




######################################################
### 63.3

def czyPopierwsza(x):
    ilosc = 0
    k = 0

    for i in range(2, x - 1):
        if x % i == 0:
            ilosc += 1
            k = i
            for z in range(2, k - 1):
                if k % z == 0:
                    return False

    if ilosc == 2:
        return True
    if ilosc == 1:
        for i in range(2 , k-1):
            if k % i != 0:
                return False
        return True

ilosc1 = 0

minn = int(Ciagi10[i])
maks = 0
for i in range(len(Ciagi10)):
    if czyPopierwsza(int(Ciagi10[i])):
        ilosc1 += 1
        if Ciagi10[i] > maks:
            maks = int(Ciagi10[i])

        if Ciagi10[i] < minn:
            minn = int(Ciagi10[i])



print(ilosc1)
print()
print(minn)
print(maks)

