def rozklad(n):
    i = 2
    arr = []
    while n != 1:
        while n % i == 0:
            n = n / i
            arr.append(i)
        i += 1
    return arr


def rozklad(n):
    czynniki = []
    dzielnik = 2
    while n > 1:
        if n % dzielnik == 0:
            czynniki.append(dzielnik)
            n = n / dzielnik
        else:
            dzielnik += 1
    return czynniki


n = input('Podaj liczbe naturalna: ')
while not n.isdecimal():
    n = input('Blad. Podaj liczbe naturalna: ')
n = int(n)

print(rozklad(n))