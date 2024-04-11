def czy_parzysta(liczba):
    return liczba % 2 == 0


a = input('Podaj liczbe naturalna: ')
a = int(a)
if 99 < a < 1000:
    s = a // 100
    if czy_parzysta(s):
        print('cyfra setek jest parzysta')
    else:
        print('cyfra setek jest nieparzysta')
else:
    print('liczba nie jest trzycyfrowa')