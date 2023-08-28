# Utilizatorul introduce un an ca input
an = int(input("Introduceti un an: "))

# Verificăm dacă anul este bisect
if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    # Dacă anul este divizibil cu 4 și nu este divizibil cu 100, sau este divizibil cu 400,
    # atunci este un an bisect
    print("Anul", an, "este bisect.")
else:
    # În caz contrar, anul nu este bisect
    print("Anul", an, "nu este bisect.")
