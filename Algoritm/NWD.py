def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

def Czypalindrom(x):
    if x == x[::-1]:
        return True
    else:
        return False

def palindrom(x):
    return x == x[::-1]

print(palindrom("aaaa"))