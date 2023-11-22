def f(x):
    return x**4/500 - x*x/200 - 3/250


def g(x):
    return -(x**3)/30 + x/20 + 1/6


prosta1 = g(10)
prosta2 = f(10)
pole1 = 0
pole2 = 0
xp = 2
xk = 10
n = 1000
dx = (xk - xp)/n
srodek = xp + ((xk - xp)/2*n)
for i in range(n):
    pole1 += abs(prosta1)-abs(g(srodek + i*dx))
    pole2 += abs(prosta2)-abs(f(srodek + i*dx))

print(pole1, pole2)
pole1 = pole1*dx
pole2 = pole2*dx
pprostokata = abs(g(10) - f(10))*8
print(pprostokata - pole1 - pole2)