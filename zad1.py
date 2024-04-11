def pitagorejskie(a, b, c):
    return (a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a)


def pitagorejskie2(a, b, c):
    lista = [a, b, c]
    lista.sort()
    return lista[0]*lista[0]+xlista[1]*lista[1]==lista[2]*lista[2]


def sprawdzenie():
    x = input('Podaj liczbe naturalna: ')
    while not x.isdecimal():
        x = input('Blad. Podaj liczbe naturalna: ')
    x = int(x)
    return x


# a = sprawdzenie()
# b = sprawdzenie()
# c = sprawdzenie()
#
# odp = pitagorejskie2(a,b,c) and "są" or "nie są"
# print(f'Podane liczby {odp} trojkami pitagorejskimi')

for i in range(1, 11):
    for j in range(i, 11):
        for k in range(j, 11):
            if pitagorejskie(i, j, k):
                print(i, j, k)