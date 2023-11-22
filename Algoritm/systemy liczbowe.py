liczba = input("podaj liczbe : ")

systemNow = int(input("podaj system w jakim jest liczba: "))
system = int(input("podaj system na  jaki chcesz zamienić: "))


def konwertowanieNa10(liczba, system):
    Liczba10 = 0
    for i in range(len(liczba)):
        if ord(liczba[i]) < 58:
            Liczba10 += int(liczba[i]) * system**(len(liczba)-i-1)
        else:
            Liczba10 += int(ord(liczba[i])-55) * system ** (len(liczba) - i-1)

    return Liczba10


def KonwertowanieNaDowolny(liczba, system):
    nowaLiczba = ''
    while liczba:
        reszta = liczba % system
        if reszta > 9:
            nowaLiczba += str(chr(reszta + 55))
        else:
            nowaLiczba += str(reszta)
        liczba = liczba // system

    return ''.join(reversed(nowaLiczba))


print(KonwertowanieNaDowolny(konwertowanieNa10(liczba, systemNow),system))




