def a():
    file = open("tekst.txt")
    lines = file.read().split()
    file.close()
    ile=0
    for i in range(len(lines)):
        checker = False
        for j in range(len(lines[i])-1):
            if lines[i][j] == lines[i][j+1]:
                checker = True
        if checker:
            ile +=1
    print(ile)



def b():
    file = open("tekst.txt")
    lines = file.read().split()
    file.close()
    ile = 0
    tab = []
    litery = 0
    for j in range(26):
        tab.append(0)
    for i in range(len(lines)):
        litery+=len(lines[i])
        for j in range(len(lines[i])):
            tab[ord(lines[i][j]) - ord("A")]+=1
    pom = 0
    for x in range(65,91):
        print(chr(x),":"," ",tab[pom]," ","(",float(round(tab[pom]/litery*100,2)),"%",")",sep='')
        pom+=1



def c():
    file = open("tekst.txt")
    lines = file.read().split()
    file.close()
    ile = 0
    max=0
    pom = []
    for i in range(len(lines)):
        k = 0
        for j in range(len(lines[i])):
            if lines[i][j] != 'A' and lines[i][j]!='E' and lines[i][j]!='O' and lines[i][j]!= 'I' and lines[i][j] != 'U' and lines[i][j]!= 'Y':
                k+=1
                if k > max:
                    max = k
                if k == 4:
                    pom.append(lines[i])
            else:
                k=0
    print(max)
    print(len(setList(pom)))
    print(pom[0])

def setList(lista):
    return list(set(lista))

c()