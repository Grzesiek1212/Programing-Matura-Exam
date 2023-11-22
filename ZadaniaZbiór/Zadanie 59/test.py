F = open("liczby.txt")

we = []

for line in F:
    x = line.rstrip()
    we.append(int(x))



odpa = 0


def rozkladLepiej(liczba):
    if liczba % 2 == 0:
        return False

    czynnik = 3
    listaUnikalnych = []
    while liczba > 1:
        if liczba % czynnik == 0:
            liczba //= czynnik
            # print(czynnik)
            if czynnik not in listaUnikalnych:
                listaUnikalnych.append(czynnik)

        if len(set(listaUnikalnych)) > 3:
            return False
        else:
            czynnik += 2
    return listaUnikalnych

print(rozkladLepiej(715520512))

#for i in range(len(we)):
#    if len(rozkladLepiej(int(we[i]))) == 3:
#        odpa += 1
#print(odpa)