def sprawdz(tekst):
    licznika = 0
    for litera in tekst:
        if litera.upper() == 'A':
            licznika += 1
    return licznika
def czy_litera(tekst, litera):
    return litera in tekst

def miejsce_spacji(tekst):
    return tekst.index(' ')

tekst = input('Podaj dowolną liczbę: ')
print(f'Liczba liter "a" {sprawdz(tekst)}')
print(tekst.lower().count('a'))
print(f'Indeks spacji: {miejsce_spacji(tekst)}')