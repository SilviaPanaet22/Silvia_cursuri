# introducem un an
an = int(input("Introduceti un an: "))
# punem conditiile
if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):  #Dacă anul este divizibil cu 4 și nu este divizibil cu 100, sau este divizibil cu 400,

      print("Anul", an, "este bisect.")
else:
    # alfel,  anul nu este bisect
    print("Anul", an, "nu este bisect.")
