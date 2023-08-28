
nume = input("Introduceti numele dumneavoastra")

while nume.isalpha() is False: #verific dacă numele conține doar litere
    nume= input("Numele este  invalid, Introduceti numele dumneavoastra")

text = input("Introduceti un text: ")

if text.isalpha() is True : #Verific dacă textul conține doar litere
    print("Sirul de numere a fost gasit de", nume)
elif text.isnumeric() is True: # dacă textul conține doar cifre
    print("Sirul de caractere a fost gasit de", nume)
else: # acă textul conține caractere alfanumerice
    print("sirul introdus de dumneavoastra este alfanumeric")
