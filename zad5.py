def czyPierwsza(n):
    licznik = 0
    for i in range(1, n + 1):
        if n % i == 0:
            licznik += 1
    return licznik == 2


# FUNKCJA OPTYMALNA OBOWIĄZUJĄCA
def czyPierwsza2(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def sprawdzenie():
    x = input('Podaj liczbe naturalna: ')
    while not x.isdecimal():
        x = inpute('Błąd. Podaj liczbe naturalna: ')
    x = int(x)
    return x

n = sprawdzenie()
print(f'Czy liczba jest pierwsza? {czyPierwsza(n)}')
print(f'Czy liczba jest pierwsza? {czyPierwsza2(n)}')