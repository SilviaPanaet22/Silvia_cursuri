def validare_cnp(cnp):
    if len(cnp) != 13:
        return "CNP-ul trebuie să conțină exact 13 cifre."

    suma = sum(int(cifra) for cifra in cnp[:12]) # Calculăm suma cifrelor primele 12 cifre ale CNP-ului.
    cifra_control_calculata = suma % 11  # Calculăm cifra de control.

    cifra_control_real = int(cnp[-1]) # Obținem cifra de control reală din ultima poziție a CNP-ului.

    if cifra_control_calculata == cifra_control_real: # Verificăm dacă cifra de control calculată este aceeași cu cifra de control reală.
        return "CNP-ul este valid."
    else:
        return "CNP-ul este invalid. Cifra de control nu corespunde."


cnp_input = input("Introduceți un CNP pentru validare: ")
rezultat = validare_cnp(cnp_input)
print(rezultat)

