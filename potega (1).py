def potega2(n):
    n = int(n)
    dwa = 1
    for i in range(1, n + 1):
        dwa = dwa * 2
    return dwa


def potega_rzeczywistej(a2, n2):
    wynik = 1
    for i in range(1, n2 + 1):
        wynik = wynik * a2
    return wynik


n = input('Podaj liczbe naturalna dodatnia')
while not n.isdecimal():
    n = input('Blad. Podaj liczbe naturalna dodatnia')
a = float(input('Podaj podstawe potegi'))
print(potega_rzeczywistej(n, a))
print(potega2(n))
