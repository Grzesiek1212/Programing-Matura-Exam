F = open("napisy.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def czyPolindrom(x):
    if x == x[::-1]:
        return True
    else:
        return False

haslo = ''
for i in range(len(Dane)):
    noweslowo = Dane[i] + Dane[i][0]
    if czyPolindrom(noweslowo):
        haslo += Dane[i][25]
    noweslowo2 = Dane[i][49] + Dane[i]
    if czyPolindrom(noweslowo2):
        haslo += Dane[i][24]

print(haslo)