haslo = input('Podaj haslo: ')
def czy_len_parzysty(haslo):
    return not bool(len(haslo) % 2)

def czy_palindrom(haslo):
    return haslo == haslo[::-1]

def czy_220(haslo):
    for i in range(0, len(haslo)-1):
        if (ord(haslo[i])) + ord(haslo[i + 1]) == 220:
            return f'{haslo[i]}, {haslo[i + 1]} spelniaja warunek.'
    return 'Zadna para nie spelnia warunku.'

def alfabet():
    for i in range(0, 26):
        print(chr(97+i), end=" ")

def czy_pierwsza_i_ostatnia(haslo):
    return haslo[0] == haslo[-1]



print(haslo[-1])
print(haslo[:5])
print(haslo[5:])
print(haslo[::2])


print(czy_len_parzysty(haslo))
print(czy_palindrom(haslo))
print(czy_220(haslo))
alfabet()
print('\n')
print(czy_pierwsza_i_ostatnia(haslo))
print(haslo.endswith('kota'))