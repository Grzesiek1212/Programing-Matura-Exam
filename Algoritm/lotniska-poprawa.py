dane = open("pasy.txt").readlines()

for i in range(len(dane)):
    dane[i] = dane[i].split()
for i in range(len(dane)):
    for j in range(len(dane[i])):
        dane[i][j] = int(dane[i][j])


#print(dane)

def zad1():
    ind = 0
    pom = []
    while ind < len(dane):
        while dane[ind] != []:
            pom.append(dane[ind])
            ind += 1
        ind += 13
        for i in range(len(pom)):
            kat = pom[i][2]
            for j in range(i+1, len(pom)):
                if kat == pom[j][2]:
                    if kat == 360:
                        if pom[i][0] > pom[j][0]:
                            print(f'{pom[i]} R {pom[j]} L')
                        else:
                            print(f'{pom[j]} R {pom[i]} L')
                    elif kat == 180:
                        if pom[i][0] < pom[j][0]:
                            print(f'{pom[i]} R {pom[j]} L')
                        else:
                            print(f'{pom[j]} R {pom[i]} L')
                    elif kat == 90:
                        if pom[i][1] < pom[j][1]:
                            print(f'{pom[i]} R {pom[j]} L')
                        else:
                            print(f'{pom[j]} R {pom[i]} L')
                    elif kat == 270:
                        if pom[i][1] > pom[j][1]:
                            print(f'{pom[i]} R {pom[j]} L')
                        else:
                            print(f'{pom[j]} R {pom[i]} L')
        pom = []

zad1()


def zad2():
    i = 0
    ilosc = 0
    pasy = []
    while i < len(dane):
        if dane[i] == []:
            if (360 in pasy and 90 in pasy) or (180 in pasy and 90 in pasy) or (360 in pasy and 270 in pasy) or (180 in pasy and 170 in pasy):
                ilosc += 1
            pasy = []
            i += 1
            continue
        pasy.append(dane[i][2])
        i += 1
    print(ilosc)

def zad3():
    i = 0
    pasy_fiz = []
    pom = []
    while i < len(dane):
        if dane[i] == []:
            i += 1
            pasy_fiz.append(len(pom))
            pom = []
            continue
        ind = str(dane[i][0]) + " " + str(dane[i][1])
        if ind not in pom:
            pom.append(ind)
        i += 1
    print(max(pasy_fiz), min(pasy_fiz))
