def dzielniki(n):
    dzielniki = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dzielniki += 1
    return dzielniki


n = input('Podaj liczbę naturalną: ')
while not n.isdecimal():
    n = input('Blad. Podaj liczbe naturalna: ')
n = int(n)
print("Liczba dzielników:", dzielniki(n))
