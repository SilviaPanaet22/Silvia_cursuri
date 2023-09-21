def separa_lista(lista, lungime_prima_lista):
    if lungime_prima_lista < 0 or lungime_prima_lista > len(lista):
        raise ValueError("Lungimea primei liste trebuie să fie între 0 și lungimea listei date.")

    prima_lista = []
    a doua_lista = []

    for i, element in enumerate(lista):
        if i < lungime_prima_lista:
            prima_lista.append(element)
        else:
            a doua_lista.append(element)

    return (prima_lista, a doua_lista)

# Exemplu de utilizare:
list_example = [1, 1, 2, 3, 4, 4, 5, 1]
first_list_length = 3
result = separa_lista(list_example, first_list_length)
print("Rezultat:", result)
