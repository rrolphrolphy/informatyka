a=input('Podaj liczbe naturalna trzycyfrowa:')
while not a.isdecimal():
    a=input('Podaj poprawna liczbe (Naturalna trzycyfrowa)')
a1=int(a)
wynik=0
while not 99<a1<1000:
    a=input('Podaj poprawna liczbe (Naturalna trzycyfrowa)')
wynik=wynik+a1%10
wynik=wynik+a1%10
wynik=wynik+a1//10
print(f'suma cyfr= {wynik}')