
cnp = input("Introduceți CNP-ul: ")

def valid_cnp(cnp):
    #  dacă CNP-ul este format doar din cifre și are lungimea corectă
    if not cnp.isdigit() or len(cnp) != 13:
        return False

    luna = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    an = int(cnp[1:3])  # Extrag anul

    # prima cifră din CNP este în intervalul [1, 9]
    if not ('1' <= cnp[0] <= '9'):
        return False
    # Verificăm dacă luna din CNP este validă
    if cnp[3:5] not in luna:
        return False

    zi_cnp = int(cnp[5:7])  # Extragem ziua din CNP

    # Verific validitatea zilei de naștere în funcție de lună și an
    if zi_cnp == 0 or (
            zi_cnp > 31 and (cnp[3:5] == '01' or cnp[3:5] == '03' or cnp[3:5] == '05' or cnp[3:5] == '07' or cnp[3:5] == '08' or cnp[3:5] == '10' or cnp[3:5] == '12')) or (
            zi_cnp > 30 and (cnp[3:5] == '04' or cnp[3:5] == '06' or cnp[3:5] == '09' or cnp[3:5] == '11')) or (
            zi_cnp > 29 and cnp[3:5] == '02') or (zi_cnp > 28 and cnp[3:5] == '02' and an % 4 != 0):
        return False

    judet_cnp = int(cnp[7:9])  # Extragem codul județului din CNP

    # Verificăm validitatea codului județului
    if judet_cnp not in range(1, 47) and judet_cnp != 51 and judet_cnp != 52:
        return False

    nnn = cnp[9:12]  # Extragem ultimele trei cifre din CNP

    # Verificăm dacă ultimele trei cifre sunt '000'
    if nnn == '000':
        return False

    cnp_validare = list(map(int, cnp))  # Convertim CNP-ul într-o listă de cifre
    nr_validare = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    c_cal = sum(x * y for x, y in zip(cnp_validare, nr_validare))  # Calculăm suma produselor dintre cifrele CNP-ului și cifrele de validare cu functia zip
    c_control = c_cal % 11
    if c_control == 10:
        c_control = 1

    return c_control == cnp_validare[-1]  # Verificăm dacă cifra de control corespunde


# Verificăm și afișăm
if valid_cnp(cnp):
    print(f"CNP-ul {cnp} este valid.")
else:
    print(f"CNP-ul {cnp} nu este valid.")
