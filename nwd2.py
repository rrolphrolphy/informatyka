a = input('Podaj liczbę naturalną: ')
while not a.isdecimal():
    a = input('Błąd. Podaj liczbę naturalną: ')
a = int(a)

b = input('Podaj liczbę naturalną: ')
while not b.isdecimal():
    b = input('Błąd. Podaj liczbę naturalną: ')
b = int(b)

a1 = a
b1 = b

if a == 0 and b == 0:
    print('Nie działa dla dwóch zer.')
    exit()
elif a == 0:
    nwd = b
else:
    while b > 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    nwd = a
nww = a1*b1//nwd
print(f'NWW: {nww}')    