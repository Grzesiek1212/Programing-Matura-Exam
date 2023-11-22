F = open("napisy.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())




ilosc = 0
for wyraz in  Dane:
    for i in range(len(wyraz)):
        if wyraz[i] in "0123456789":
            ilosc += 1

        # if wyraz[i].isdigit():
        #     if wyraz[i].isnumeric():
        # if not (ord('A') <= ord(wyraz[i]) <= ord('Z'))


print(ilosc)
