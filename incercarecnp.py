def validate_cnp(cnp):
    # Verificăm dacă CNP-ul are exact 13 cifre
    if len(cnp) != 13:
        print("CNP-ul trebuie să aibă exact 13 cifre")

    constanta = "279146358279"
    total_suma = 0

    for i in range(12):
        total_suma += int(cnp[i]) * int(constanta[i])

    restul_impartirii = total_suma % 11

    if restul_impartirii == 10:
        return control_digit = 1
    else:
        return  restul_impartirii


# Verificăm dacă cifra de control calculată corespunde cu cifra din CNP
    if control_digit != int(cnp[12]):
        return "Cifra de control este incorectă"

    return "CNP-ul este valid"

cnp = input("Introduceți CNP-ul: ")
validation_result = validate_cnp(cnp)

print(validation_result)
