def G(x):
    return (-(x**3/30)+ x/20 + 1/6)

def F(x):
    return x**4/500 - x**2/200 - 3/250

def Dlugosc(x,y , z ,m):
    return ((x-z)**2 + (y-m)**2)**(1/2)

import math

dlugosc = 0
xP = 2
xK = 10
n = int(8/(1/4))

dx = (xK - xP)/n

for i in range(n):
    dlugosc += math.floor(Dlugosc(xP + i * dx, F(xP + i * dx), xP + i * dx, G(xP + i * dx)))

print(dlugosc)
