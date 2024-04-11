import random
num = random.randint(1, 10)
while True:
    ans = int(input('Zgadnij liczbe: '))
    if num == ans:
        print(f'Poprawna odpowiedź. Liczba to {ans}')
        break
    elif ans > num:
        print('Liczba jest mniejsza od podanej.')
    else:
        print('Liczba jest większa od podanej.')