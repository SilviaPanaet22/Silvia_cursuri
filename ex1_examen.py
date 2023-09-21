def functie_lista(x: list, k: int) -> list:
    lista_noua = x[:-k-1:-1]
    lista_noua.reverse()
    for i, v in enumerate(x):
        if i < len(x)-k:
            lista_noua.append(v)
    return lista_noua


lista = input("Introduceti o lista de numere: ")
lista = lista.split()
while any(not x.isdigit() for x in lista) or len(lista) == 0:
    lista = input("Introduceti o lista de numere: ")
    lista = lista.split()
value_left_move = input("Introduceti cate elemente sa fie mutate in stanga: ")
while value_left_move.isdigit() is False or int(value_left_move) > len(lista):
    value_left_move = input("Valoare invalida.Introduceti cate elemente sa fie mutate in stanga: ")
print(*functie_lista(lista, int(value_left_move)))