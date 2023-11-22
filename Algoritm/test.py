trojkaty = [int(i) for i in open("dane_trojkaty.txt").read().split()]


############## 80 1
def czy_prostokatny(l1, l2, l3):
    tab = [l1, l2, l3]
    tab.sort()
    a, b, c = tab[0], tab[1], tab[2]
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False


for i in range(len(trojkaty) - 2):
    if czy_prostokatny(trojkaty[i], trojkaty[i + 1], trojkaty[i + 2]):
        print(trojkaty[i], trojkaty[i + 1], trojkaty[i + 2])
print()


############## 80 2
def czy_trojkat(l1, l2, l3):
    tab = [l1, l2, l3]
    tab.sort()
    a, b, c = tab[0], tab[1], tab[2]
    return a + b > c


pomoc = [sorted(trojkaty)[-i - 1] for i in range(len(trojkaty))]
maxi = 0
for i in range(len(pomoc) - 2):
    if czy_trojkat(pomoc[i], pomoc[i + 1], pomoc[i + 2]):
        l = pomoc[i] + pomoc[i + 1] + pomoc[i + 2]
        if l > maxi:
            maxi = l
print(maxi)
print()
########## 80 3
odp3 = []
pomoc = sorted(trojkaty)
for i in range(498):
    a = pomoc[i]
    for j in range(i + 1, 499):
        b = pomoc[j]
        maxc = a + b
        k = j + 1
        while pomoc[k] < maxc and k < 500:
            odp3.append(sorted([pomoc[i], pomoc[j], pomoc[k]]))
            k += 1
print(len(odp3))