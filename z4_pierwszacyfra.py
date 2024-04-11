a = int(input('Wprowadz naturalna liczbe trzycyfrowa: '))
if not (a >= 100 and a <= 999):
    print('Podano niepoprawna liczbe!')
    exit()
if ((a // 100) % 2 == 0):
    print('Pierwsza cyfra jest parzysta')
else:
    print('Pierwsza cyfra nie jest parzysta')