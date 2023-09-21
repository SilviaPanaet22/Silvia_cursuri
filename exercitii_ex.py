#1
nr_chei = input("Introduceti nr chei care sa fie maxim 20: ")
while nr_chei.isdigit() is False or int(nr_chei) not in range(21):
    nr_chei = input("Introduceti nr chei care sa fie maxim 20: ")
dictionar = {}
for index in range(1,int(nr_chei)+1):
    dictionar.update({f'{index}': index **2})
print(dictionar)

#2
def suma_tuplu(tuplu):
    suma = 0
    for numar in tuplu:
        suma += numar
    return suma

# Exemplul dat :
tuple_example = (8, 2, 3, 0, 7)
result = suma_tuplu(tuple_example)
print("Suma elementelor din tuplu este:", result)


#3
def separere_lista(lista: list, nr: int) -> list:
    rezultat =[]
    rezultat.append(lista[0:nr])
    rezultat.append(lista[nr:])
    return rezultat


lista_exemplu = [1, 1, 2, 3, 4, 4, 5, 1]
nr = input("Introduceti numarul: ")
while nr.isdigit() is False or int(nr) > len(lista_exemplu):
    nr = input("Introduceti numarul: ")
print(separere_lista(lista_exemplu, int(nr)))

#4
def numara_vocale(sir):
    vocale = "aeiou"
    numar_vocale = 0

    for litera in sir:
        if litera in vocale:
            numar_vocale += 1

    return numar_vocale

# Exemplu :
sir = "inginer"
rezultat = numara_vocale(sir)
print("Numărul de vocale din șir este:", rezultat)


#5


x = int(input("introduceti primul nr  "))
y = int(input("introduceti al doilea nr  "))
z = int(input("introduceti al treilea nr  "))
if x==0 or y==0 or z==0:
    print(0)
elif x==y==z:
    print(3*x/y/z)
else:
    print(x/y/z)

#6
def dublul_pare(sir):
    rezultat = []
    for numar in sir:
        rezultat.append(numar)

        if numar % 2 == 0:
            dublu = numar * 2
            rezultat.append(dublu)
    return rezultat
# Exemplu:
sir = [1, 2, 3, 4, 5, 6, 7]
rezultat = dublul_pare(sir)
print("Șirul rezultat este:", rezultat)

