import random


def suma_cyfr1(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma


n = int(random.random() * 1000000)
print(n)
print('suma cyfr = ', suma_cyfr1(n))