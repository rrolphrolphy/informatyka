def czy_parzysta_binarna(liczba_binarna):

    if not liczba_binarna.isdigit():
        print("Podana wartość nie jest liczbą binarną.")

    suma = 0
    for cyfra in liczba_binarna:
        suma += int(cyfra)

    return suma % 2 == 0

liczba_binarna = input("Podaj liczbę binarną: ")

if czy_parzysta_binarna(liczba_binarna):
    print(f"Liczba {liczba_binarna} jest parzysta.")
else:
    print(f"Liczba {liczba_binarna} jest nieparzysta.")