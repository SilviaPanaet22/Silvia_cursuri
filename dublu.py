def insereaza_dublul_pentru_pare(sir):
    rezultat = []  # Inițializăm o listă goală pentru a stoca rezultatul

    for numar in sir:
        rezultat.append(numar)  # Adăugăm numărul curent în rezultat

        if numar % 2 == 0:
            dublu = numar * 2  # Calculăm dublul pentru numerele pare
            rezultat.append(dublu)  # Adăugăm dublul în rezultat

    return rezultat


# Exemplu de utilizare:
sir = [1, 2, 3, 4, 5, 6, 7]
rezultat = insereaza_dublul_pentru_pare(sir)
print("Șirul rezultat este:", rezultat)
