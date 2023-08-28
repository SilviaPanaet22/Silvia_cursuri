def validare_cnp(cnp):

    if len(cnp) != 13:  # Verificăm dacă CNP-ul are exact 13 cifre
        return "CNP-ul trebuie să aibă exact 13 cifre"

    constanta = "279146358279" # constanta cu care trebuie sa inmultim
    total_suma = 0 # initializam variabila cu 0

    for i in range(12):
        total_suma += int(cnp[i]) * int(constanta[i]) # inmultim fiecare cifra din cnp-ul introdus cu fircare cifra din constanta

    restul_impartirii = total_suma % 11 #facem restul impartirii

    if restul_impartirii == 10: # verificam conditia daca restul impartiiri este 10, cifra de control va fi 1
        cifra_control = 1
    else:
        cifra_control=cnp[-1] #  altfel cifra de control este ultima cifra din cnp


    if cifra_control != int(cnp[12]): # Verificăm dacă cifra de control calculată este egala cu ultima cifra din cnp
        return "Cifra de control este incorectă"

    return "CNP-ul este valid"

cnp = input("Introduceți CNP-ul: ") #introduc cnp-ul
rezultatul_validarii = validare_cnp(cnp) # apelez functia

print(rezultatul_validarii) # afisez rezultatul
