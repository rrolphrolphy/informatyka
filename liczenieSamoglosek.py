def policz_samogloski(text):
  samogloski = "aeiouy"
  liczba_samoglosek = 0

  for znak in text.lower():
    if znak in samogloski:
      liczba_samoglosek += 1

  return liczba_samoglosek

tekst = input("Podaj tekst: ")
liczba_samoglosek = policz_samogloski(tekst)

print(f"W podanym tekście jest {liczba_samoglosek} samogłosek.")