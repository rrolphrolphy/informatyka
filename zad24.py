licznik1 = input('Podaj licznik 1: ')
while not licznik1.isdecimal():
    licznik1 = input('Blad. Podaj licznik 1: ')
licznik1 = int(licznik1)

mianownik1 = input('Podaj mianownik 1: ')
while not (mianownik1.isdecimal() and mianownik1 != "0"):
    mianownik1 = input('Blad. Podaj mianownik 1: ')
mianownik1 = int(mianownik1)

licznik2 = input('Podaj licznik 2: ')
while not licznik2.isdecimal():
    licznik2 = input('Blad. Podaj licznik 2: ')
licznik2 = int(licznik2)

mianownik2 = input('Podaj mianownik 2: ')
while not (mianownik2.isdecimal() and mianownik2 != "0"):
    mianownik2 = input('Blad. Podaj mianownik 2: ')
mianownik2 = int(mianownik2)

lSc = licznik1 * licznik2
mSc = mianownik1 * mianownik2

lScb = lSc
mScb = mSc

if lSc == 0 and mSc == 0:
    print('Nie działa dla dwóch zer.')
else:
    while mSc > 0:
        lSc, mSc = mSc, lSc%mSc

lScb = int(lScb) / int(lSc)
mScb = int(mScb) / int(lSc)

lScb = int(lScb)
mScb = int(mScb)

if lScb > mScb:
    first = lScb // mScb
    lScb = lScb - mScb
    print(f'Wynik: {first} i {lScb}/{mScb}')
else:
    print(f'Wynik: {lScb}/{mScb}')