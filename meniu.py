# scriu meniul
meniu = """
1 - Afisare lista de cumparaturi
2 - Adaugare element
3 - Stergere element
4 - Stergere lista de cumparaturi
5 - Cautare in lista de cumparaturi
"""
print(meniu)# Afisez meniul
numar_selectat = int(input("Introduceti un numar intre 1 si 5: ")) # citesc numarul introdus

if numar_selectat == 1: # Verific ce optiune selectez
    print("Afisare lista de cumparaturi")
elif numar_selectat == 2:
    print("Adaugare element")
elif numar_selectat == 3:
    print("Stergere element")
elif numar_selectat == 4:
    print("Stergere lista de cumparaturi")
elif numar_selectat == 5:
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")
