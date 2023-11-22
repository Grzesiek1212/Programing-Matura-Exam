def sumaCyfr(x):
    suma = 0
    while x:
        suma += x % 10
        x = x // 10
    return suma

