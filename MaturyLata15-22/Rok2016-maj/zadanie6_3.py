F = open('dane_6_3.txt')
Dane = []

for line in F:
    Dane.append(line.split())



for pary in Dane:
    klucze = []
    a = pary[0]
    b = pary[1]
    klucz = 0
    for i in range(len(a)):
        klucze.append(ord(b[i])-ord(a[i]))

    for i in range(len(klucze)):
        if klucze.count(klucze[i]) > klucze.count(klucz):
            klucz = klucze[i]
    noweslowo = ''
    while klucz > 26:
        klucz -= 26

    if klucz > 0:
        for i in range(len(a)):
            numer = ord(a[i]) + klucz
            if numer > ord('Z'):
                numer -= 26
            noweslowo += chr(numer)
    else:
        for i in range(len(a)):
            numer = ord(a[i]) + klucz
            if numer < ord('A'):
                numer += 26
            noweslowo += chr(numer)
    if b != noweslowo:
        print(a)



