def G(x):
    return abs(-(x**3/30)+ x/20 + 1/6)

def F(x):
    return x**4/500 - x**2/200 - 3/250

poleprostokata = (F(10)+G(10))*8

pole2 = 0
pole1 = 0
xP = 2
xK = 10
n = 1000

dx = (xK - xP)/n

for i in range(n):
    pole1 += G(10) - G(xP+((i+1)*dx))
    pole2 += F(10) - F(xP+(i+1)*dx)

pole1 = (pole1 + (G(xP)+G(xK))/2) * dx
pole2 = (pole2 + (F(xP)+F(xK))/2) * dx

def pod_a():
    a = 2
    b = 10
    n = 1000
    suma_h_g = 0
    suma_h_f = 0
    srodek = a + ((b - a)/(2*n))
    for i in range(n):
        suma_h_g += abs(g(10)) - abs(g(srodek + i*((b-a)/n)))
        suma_h_f += abs(f(10)) - abs(f(srodek + i*((b-a)/n)))
    Pole = ((b-a)/n) * suma_h_g + ((b-a)/n) * suma_h_f
    print(round(ABCD - Pole, 3))

print(round(poleprostokata - (pole1+pole2),3))
