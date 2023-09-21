def rotire_stanga(lista: list, k: int) -> list:
    if k > len(lista):
        print("K e mai mare decat lista ta")
        return lista
    if any(not str(k).isdigit() for k in lista):
        return "Eroare, vezi ca aceasta lista nu conține doar numere întregi."
    return lista[-k::] + lista[:-k]

lista1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rezultat1 = rotire_stanga(lista1, k1)
print(rezultat1)

lista2 = [1, 100, 3, 99]
k2=3
rezultat2 = rotire_stanga(lista2, k2)
print(rezultat2)