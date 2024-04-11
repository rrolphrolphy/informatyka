def dzielnikiN(n):
    lista=[]
    for i in range(1, n+1):
        if n % i == 0:
            lista.append(i)
    return lista


def sprawdzenie():
    x = input('Podaj liczbe naturalna: ')
    while not x.isdecimal():
        x = inpute('Błąd. Podaj liczbe naturalna: ')
    x = int(x)
    return x


n = sprawdzenie()
print(dzielnikiN(n))