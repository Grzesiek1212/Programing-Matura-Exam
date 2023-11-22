we = open("trojki.txt")
liczby = []
for line in we:
    p = line.split()
    for i in range(len(p)):
        p[i] = int(p[i])
    liczby.append(p)


######### 66 1
def suma_cyfr(n):
    suma = 0
    while n:
        suma += n % 10
        n //= 10
    return suma


for i in liczby:
    if suma_cyfr(i[0]) + suma_cyfr(i[1]) == i[2]:
        print(i)
print()


######## 66 2
def czy_pierwsza(n):
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


for i in liczby:
    if czy_pierwsza(i[0]) and czy_pierwsza(i[1]) and i[0] * i[1] == i[2]:
        print(i)
print()


############ 66 3
def czy_prostokat(t):
    pomoc = []
    for i in t:
        pomoc.append(i)
    pomoc.sort()
    a, b, c = pomoc[0] ** 2, pomoc[1] ** 2, pomoc[2] ** 2
    return a + b == c


for i in range(len(liczby)):
    if czy_prostokat(liczby[i]) and czy_prostokat(liczby[i + 1]):
        print(liczby[i], liczby[i + 1])
print()


######### 66 4
def czy_trojkat(t):
    if t[0] + t[1] > t[2] and t[2] + t[1] > t[0] and t[0] + t[2] > t[1]:
        return True
    return False


odpd = 0
dlg = 0
maxi = 0
for i in liczby:
    if czy_trojkat(i):
        dlg += 1
        odpd += 1
        if dlg > maxi:
            maxi = dlg
    else:
        dlg = 0
print(odpd, maxi)