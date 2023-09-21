def rotatie_stanga(lista, k):
    n = len(lista)

    if k > n:
        return "Eroare: Valoarea lui k este mai mare decât numărul de elemente din lista."

    lista[:] = lista[k:] + lista[:k]

def main():
    lista = input("Introduceti o lista de numere separate prin spatii: ").split()
    k = int(input("Introduceti cate elemente sa fie mutate in stanga: "))

    if k > len(lista):
        print("Eroare: Valoarea lui k este mai mare decât numărul de elemente din lista.")
    else:
        rotatie_stanga(lista, k)
        print("Lista rezultata:", lista)

if __name__ == "__main__":
    main()
