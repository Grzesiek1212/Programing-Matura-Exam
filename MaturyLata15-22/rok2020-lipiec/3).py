F = open("identyfikator.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def Suma(x):
    a = ord(x[0]) - 55
    b = ord(x[1]) - 55
    c = ord(x[2]) - 55
    d = int(x[4])
    e = int(x[5])
    f = int(x[6])
    g = int(x[7])
    h = int(x[8])
    return (7*(a+d+g) + 3 * (b+e+h)+ c + f) % 10

for i in range(len(Dane)):
    if int(Dane[i][3]) != Suma(Dane[i]):
        print(Dane[i])

