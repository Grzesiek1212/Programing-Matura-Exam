F = open("liczby.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def NWD(a, b):
    while b:
        a, b = b, a%b
    return a

najpierwszaliczba = 0
iloscmaks = 0
pierwszaLiczba = 0
najnwd =  0
ilosc = 1
nwd = NWD(int(Dane[0]),int(Dane[1]))

for i in range(2, len(Dane)):
    if NWD(nwd, int(Dane[i])) > 1:
        nwd = NWD(nwd, int(Dane[i]))
        # print(nwd, Dane[i])
        ilosc += 1
        if ilosc == 2:
            pierwszaLiczba = int(Dane[i-1])
        if ilosc > iloscmaks:
            iloscmaks = ilosc
            najnwd = nwd
            najpierwszaliczba = pierwszaLiczba
    else:
        ilosc = 1
        nwd = int(Dane[i])

print(najpierwszaliczba, iloscmaks, najnwd)

