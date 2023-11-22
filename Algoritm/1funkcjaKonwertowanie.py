liczba = input("podaj liczbe : ")

systemNow = int(input("podaj system w jakim jest liczba: "))
system = int(input("podaj system na  jaki chcesz zamienić: "))


def AnytoAny (liczba, system, systemNowy):
    Liczba10 = 0
    for i in range(len(liczba)):
        if ord(liczba[i]) < 58:
            Liczba10 += int(liczba[i]) * system**(len(liczba)-i-1)
        else:
            Liczba10 += int(ord(liczba[i])-55) * system ** (len(liczba) - i-1)

    nowaLiczba = ''
    while Liczba10:
        reszta = Liczba10 % systemNowy
        if reszta > 9:
            nowaLiczba += str(chr(reszta + 55))
        else:
            nowaLiczba += str(reszta)
        Liczba10 = Liczba10 // systemNowy

    return ''.join(reversed(nowaLiczba))


print(AnytoAny(liczba, systemNow, system))
