F = open("napisy.txt")

Napisy = []

for line in F:
    Napisy.append(line.split())

########################################################
### 72.1

ilosc = 0
k = 0
for i in range(len(Napisy)):
    x = Napisy[i][0]
    y = Napisy[i][1]
    if  int(len(x) / 3) >= len(y) or int(len(y)/3) >= len(x):
        ilosc += 1

    if ilosc == 1:
        k += 1
        if k == 1:
            print(x, y)

print(ilosc)
print("\n")

##########################################################
### 72.2

for i in range(len(Napisy)):
    x = Napisy[i][0]
    y = Napisy[i][1]
    if len(y) > len(x):
        if x == y[:len(x)]:
            print(x, y, y[len(x):])

print("\n")
####################################################
### 72.3

maks = 0

for i in range(len(Napisy)):
    x = Napisy[i][0]
    y = Napisy[i][1]
    j = min(len(x), len(y))
    for p in range(1, j):
        if x[-p] != y[-p]:
            if p == 16:
                print(x, y)
                print(len(x))
                maks = p - 1
            break





print(maks)









