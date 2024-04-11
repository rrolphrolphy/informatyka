import random
def sprawdzenie():
    x = input('Ile liczb losowac: ')
    while not x.isdecimal():
        x = input('Blad. Podaj liczbe naturalna: ')
    x = int(x)
    return x


def najwieksza(n):
    maks = 0
    for i in range(n):
        a = random.randint(1, 20)
        if a > maks:
            maks = a
    return maks
n = sprawdzenie()


def najwieksza1(tablica):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 20))
    print(arr)
    return max(arr)


print(f'Najwieksza liczba to {najwieksza(n)}')
print(f'Najwieksza liczba to {najwieksza1(n)}')