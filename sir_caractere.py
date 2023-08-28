nume = "Silvia Panaet"
text = input("Introduceti un text: ")

if text.isdigit():
    print("Sirul de numere a fost gasit de", nume)
elif isinstance(text, str):
    print("Sirul de caractere a fost gasit de", nume)
else:
    print("Nu s-a putut determina tipul de sir")
