def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

def suma(n):
    return n * (n + 1) // 2

n = input('Podaj liczbę naturalną dodatnią: ')
while not n.isdecimal() or int(n) < 1:
    n = input('Blad. Podaj liczbe naturalną dodatnią: ')
n = int(n)
wynik = suma(n) / silnia(n)
print("Wynik:", wynik)