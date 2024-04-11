n = input('Ile liczb wpisać: ')
while not n.isdecimal():
    n = input('Błąd. Podaj liczbę naturalną: ')
n = int(n)
i = 0
while i < n:
    i += 1
    print(i, end=' ')
print()
print('-' * 30)
for i in range(n, 0, -1):
    print(i, end=' ')
print()
print('-' * 30)

i = 0
while i < n:
    i += 2
    print(i, end=' ')
print()
for i in range(2, n + 1, 2):
    print(i, end=' ')