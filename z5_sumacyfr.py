a = int(input('Wprowadź naturalną liczbę dwucyfrową: '))
if (a <= 10 or a >= 99):
    print('Podano niepoprawna liczbe!')
    exit(-1)
print(f'Suma cyfr tej liczby: {a // 10 + a % 10}')