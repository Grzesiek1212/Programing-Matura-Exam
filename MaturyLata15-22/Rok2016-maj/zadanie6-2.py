F = open('dane_6_2.txt')
Dane = []

for line in F:
    Dane.append(line.split())

for pary in Dane:
    klucz = int(pary[1])
    slowo = pary[0]
    noweslowo = ''
    while klucz > 26:
        klucz -= 26
    print(klucz)
    for i in range(len(slowo)):
        numer = ord(slowo[i]) - klucz
        if numer < 65:
            numer += 26
        noweslowo += chr(numer)

    print(noweslowo)