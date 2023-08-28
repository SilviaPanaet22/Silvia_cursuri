# introduc un numar de tip float de la tastatura
numar = float(input("Introduceti un numar: "))

if numar > 0:
    # Verific dacă numărul este pozitiv și mai mic decât 10
    if numar < 10:
        print("Numarul este pozitiv și mai mic decât 10.")
    else:
        print("Numarul este pozitiv, dar nu este mai mic decât 10.")
elif numar == 0:
    # Dacă numărul este zero și afisez mesajul
    print("Numarul este 0.")
else:
    # Dacă numărul este negativ, calculăm valoarea pozitivă corespunzătoare, punand un minus in fata lui
    numar_pozitiv = -numar
    print("Numarul este negativ. Valoarea pozitivă corespunzătoare este:", numar_pozitiv)
