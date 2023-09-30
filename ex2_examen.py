def element_majoritar(lista):
    majoritare = []
    frecventa_maxima = 0

    for numar in lista:
        frecventa = lista.count(numar)
        if frecventa > frecventa_maxima:
            majoritare = [str(numar)]
            frecventa_maxima = frecventa
        elif frecventa == frecventa_maxima and str(numar) not in majoritare:
            majoritare.append(str(numar))

    if majoritare:
        return ', '.join(majoritare)
    else:
        return "Nu există element care sa fie majoritar."

#exemple
lista1 = [3, 2, 3]
rezultat1 = element_majoritar(lista1)
print(rezultat1)

lista2 = [2, 2, 1, 1, 1, 2, 2]
rezultat2 = element_majoritar(lista2)
print(rezultat2)

lista3 = [1, 2, 3, 3, 1,2,7]
rezultat3 = element_majoritar(lista3)
print(rezultat3)