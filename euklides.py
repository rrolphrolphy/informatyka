a = input('Podaj liczbę naturalną: ')
while not a.isdecimal():
    a = input('Błąd. Podaj liczbę naturalną: ')
a = int(a)

b = input('Podaj liczbę naturalną: ')
while not b.isdecimal():
    b = input('Błąd. Podaj liczbę naturalną: ')
b = int(b)

if a == 0 and b == 0:
    print('Nie działa dla dwóch zer.')
elif a == 0:
    print(f'NWD: {b}')
else:
    # while b > 0:
    #     a, b = b, a%b
    #     print(f'NWD = {a}')
    while b > 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(f'NWD = {a}')

# a = 5
# b = 8
# pomoc = a
# a = b
# b = pomoc
# print(a, b)
# a, b = b, a
# print(a, b)