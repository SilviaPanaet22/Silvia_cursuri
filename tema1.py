a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a1 = set(a)# Am convertit  listele in seturi pentru se a elimina elementele care apar de 2 ori
b1 = set(b) #converirea listei b

rezultat_set = a1 & b1 # folosesc operatorul de intersecție pentru a ajunge la rezultat
rezultat = list(rezultat_set) # Convertesc  setul care mi-a reiesit ca rezultat  într-o listă
print(rezultat) # rezultatul final sub forma de lista