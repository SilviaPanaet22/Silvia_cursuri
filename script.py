#   declarea listei inițiale
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Afișarea listei inițiale ordonată ascendent, dar păstram  lista inițială neschimbată
lista_ascendenta = sorted(lista)
print("Lista initiala ordonata ascendent:", lista_ascendenta)

# Afișarea listei inițiale ordonată descendent, dar păstram  lista inițială neschimbată
lista_descendenta = sorted(lista, reverse=True)
print("Lista initiala ordonata descendent:", lista_descendenta)

# Afișarea listei cu numere pare din lista inițială ordonată
lista_pare = lista_ascendenta[1::2]  # Se folosește slice pentru a selecta elementele pare
print("Lista cu numere pare:", lista_pare)

# Afișarea listei cu numere impare din lista inițială ordonată
lista_impare = lista_ascendenta[::2]  #slice- Aceasta selectează elementele impare din lista ordonată-  începe cu indicele 1  și ia fiecare al doilea element.
print("Lista cu numere impare:", lista_impare)

# Afișarea listei ce contine  numere ce sunt multipli ai numărului 3 din lista inițială ordonată
lista_multipli_3 = lista_ascendenta[2::3]  # selecteaz elementele din lista ordonată care sunt multipli de 3, incep  cu indicele 2 și ia fiecare al treilea element.
print("Lista ce contine numere ce  sunt  multiplii de 3:", lista_multipli_3)
