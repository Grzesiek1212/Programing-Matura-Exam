

lista = ['komputer', 'rolki', 'miś', 'lego', 'wrotki', 'skakanka', 'łóżko', 'kask' ]
lista1 = []
n = int(input("wielkosc tabeli: "))

import random

for i in range(n):
    lista1.append([lista[random.randint(0, 7)], random.random(), random.random(), random.randint(1, 3)]) ## (przedmiot, waga , cena , ilość)



for i in range(n):
    lista1[i].append(lista1[i][2]/lista1[i][1])




