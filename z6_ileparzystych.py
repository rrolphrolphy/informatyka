a = input('Wprowadz naturalna liczbe trzycyfrowa: ')
while not a.isdecimal():
    a = input('Błąd. Podaj liczbę naturalną: ')
a = int(a)
if (a <= 100 or a >= 999):
    print('Podano niepoprawna liczbe!')
    exit()
score = 0
if not ((a // 100) % 2):
    score = score + 1
if not (((a // 10) % 10) % 2):
    score = score + 1
if not ((a % 10) % 2):
    score = score + 1
print(f'Liczba cyfr parzystych: {score}')