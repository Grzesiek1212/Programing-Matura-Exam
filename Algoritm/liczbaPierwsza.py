def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True


def czyPierwsza2(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def czyPierwsza3(x):
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True


def czyPierwsza4(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


