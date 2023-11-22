# liczba = input("podaj liczbe : ")
#
# systemNow = int(input("podaj system w jakim jest liczba od 2 do 10: "))
# system = int(input("podaj system na  jaki chcesz zamienić od 2 do 10: "))


def AnyToDec(liczba, system ):
    Liczba10 = 0
    for i in range(len(liczba)):
            Liczba10 += int(liczba[i]) * system**(len(liczba)-i-1)
    return Liczba10


def DecToAny(liczba, system):
    nowaLiczba = ''
    while liczba:
        nowaLiczba += str(liczba % system)
        liczba = liczba // system

    return ''.join(reversed(nowaLiczba))


print(97-26)
