def numara_vocale(sir):
    vocale = "AEIOUaeiou"
    numar_vocale = 0

    for caracter in sir:
        if caracter in vocale:
            numar_vocale += 1

    return numar_vocale

# Exemplu de utilizare:
sir = "Exemplu"
rezultat = numara_vocale(sir)
print("Numărul de vocale din șir este:", rezultat)
