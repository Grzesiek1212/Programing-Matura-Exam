def G(x):
    return (-(x**3/30)+ x/20 + 1/6)

def F(x):
    return x**4/500 - x**2/200 - 3/250

def dlugosc(x,y , z ,m):
    return ((x-z)**2 + (y-m)**2)**(1/2)

obw1 = 0
obw2 = 0
xP = 2
xK = 10
n = 1000

dx = (xK - xP)/n

for i in range(n-1):
    obw1 += dlugosc(xP + i * dx, G(xP + i * dx), xP + (i + 1) * dx, G(xP + (i + 1) * dx))
    obw2 += dlugosc(xP + i * dx, F(xP + i * dx), xP + (i + 1) * dx, F(xP + (i + 1) * dx))


print(obw1+obw2+abs(G(10))+F(10)+16)