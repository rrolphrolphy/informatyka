import random

def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma

n = input('Podaj liczbe naturalna: ')
while not n.isdecimal():
    n = input('Blad. Podaj liczbe naturalna: ')

# print('Suma cyfr =', suma_cyfr(n))
lista = []
for i in range(n):
    lista.append(random.randint(-100, 100))
print(lista)
print('Liczba 10:', ile_10(lista))
print(lista.count(10))