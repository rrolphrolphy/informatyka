def liczba_podzielnych_przez_3(n):
    liczba_podzielnych = 0
    for i in range(n + 1):
        if i % 3 == 0:
            liczba_podzielnych += 1
    return liczba_podzielnych

n = input('Podaj liczbę naturalną: ')
while not n.isdecimal():
    n = input('Blad. Podaj liczbe naturalna: ')
n = int(n)
print("Liczba podzielnych przez 3:", liczba_podzielnych_przez_3(n))