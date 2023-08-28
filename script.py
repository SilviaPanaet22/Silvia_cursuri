#1-declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4. 10, 5, 6 (în această ordine).
# 2-afişează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
# 3-afişează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeaşi formă)
# 4-afişează o listă ce conţine numerele pare din lista ordonată (folosind slice)
# 5-afişează o listă ce conţine numerele impare din lista ordonată (folosind slice)
# 6-afisează o listă ce conţine numerele ce sunt multipli ai numărului 3 (folosind slice).

#1
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#2
lista_ascendenta = sorted(lista)
print("Lista initiala ordonata ascendent:", lista_ascendenta)

#3
lista_descendenta = sorted(lista, reverse=True)
print("Lista initiala ordonata descendent:", lista_descendenta)

#4
lista_pare = lista_ascendenta[1::2]  #slice- selectează fiecare al doilea element începând de la al doilea element din lista, pentru a selecta nr pare
print("Lista cu numere pare:", lista_pare)

# 5
lista_impare = lista_ascendenta[::2]  #slice- Aceasta selectează elementele impare din lista ordonată-  încep cu indicele 1  și iau fiecare al doilea element.
print("Lista cu numere impare:", lista_impare)

# 6
lista_multipli_3 = lista_ascendenta[2::3]  # selecteaz elementele din lista ordonată care sunt multipli de 3, incep  cu indicele 2 și iau fiecare al treilea element.
print("Lista ce contine numere ce  sunt  multiplii de 3:", lista_multipli_3)
