F = open("identyfikator.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def Czypalindrom(x):
    if x == x[::-1]:
        return True
    else:
        return False

for i in range(len(Dane)):
    if Czypalindrom(Dane[i][:3]) or Czypalindrom(Dane[i][3:]):
        print(Dane[i])