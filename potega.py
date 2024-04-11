n = input('Podaj liczbę rzeczywistą: ')
while not n.isdecimal():
    n = input('Błąd. Podaj liczbę rzeczywistą: ')
n = int(n)
print(pow(2, n))