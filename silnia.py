n = input('Podaj liczbę naturalną: ')
while not n.isdecimal():
    n  = input('Błąd. Podaj liczbę naturalną: ')
n = int(n)
silnia = 1
for i in range(2, n+1):
    silnia = silnia * i

plusSilnia = 1
for i in range(2, n+1):
    plusSilnia = plusSilnia + i

print(n, 'silnia =', silnia)
print(n, 'silnia plusowa = ', plusSilnia)