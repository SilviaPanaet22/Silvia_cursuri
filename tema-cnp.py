def validare_cnp(cnp):
    if len(cnp) != 13 or not cnp.isdigit():
        return False

    sex = int(cnp[0])
    anul_nasterii = int(cnp[1:3])
    luna = int(cnp[3:5])
    ziua = int(cnp[5:7])
    cod_judet = int(cnp[7:9])
    nnn = int(cnp[9:12])
    cifra_control = int(cnp[12])

    if sex not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False

    if sex == 9:
        anul_nasterii += 1800
    elif sex == 0 and anul_nasterii >= 0 and anul_nasterii <= 9:
        anul_nasterii += 2000
    elif sex == 0 and anul_nasterii >= 10 and anul_nasterii <= 99:
        anul_nasterii += 1900

    if anul_nasterii < 1800 or anul_nasterii > 2099:
        return False

    if luna < 1 or luna > 12:
        return False

    zile_in_luna = {
        1: 31, 2: 29 if (anul_nasterii % 4 == 0 and anul_nasterii % 100 != 0) or (anul_nasterii % 400 == 0) else 28,
        3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if ziua < 1 or ziua > zile_in_luna[luna]:
        return False

    if cod_judet < 1 or cod_judet > 52 or (cod_judet > 46 and cod_judet != 51):
        return False

    if nnn < 1 or nnn > 999:
        return False

    ponderi = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma_ponderata = sum(int(cnp[i]) * ponderi[i] for i in range(12))
    rest_div11 = suma_ponderata % 11
    cifra_control_calculata = 1 if rest_div11 == 10 else rest_div11

    if cifra_control != cifra_control_calculata:
        return False

    return True


cnp = input("Introduceți CNP-ul: ")
if validare_cnp(cnp):
    print(f"CNP-ul {cnp} este valid.")
else:
    print(f"CNP-ul {cnp} nu este valid.")
